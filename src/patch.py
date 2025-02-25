import os
import json
import re
from collections import defaultdict

def collect_json_files(directory):
    """Recursively collects all JSON files from a directory."""
    json_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
    return json_files

def extract_papers_by_venue(json_files):
    """Extracts and categorizes papers from JSON files by venue."""
    venue_dict = defaultdict(list)
    
    for json_file in json_files:
        with open(json_file, 'r', encoding='utf8') as f:
            try:
                data = json.load(f)
                for title in data:
                    paper = data[title]
                    venue = paper.get("venue", "Unknown Venue")
                    venue_dict[venue].append({
                        "title": title,
                        "author": paper.get("author", "Unknown Author"),
                        "abstract": paper.get("abstract", "No Abstract Available"),
                        "url": paper.get("url", "No Link Available"),
                        "venue": paper.get("venue"),
                        "labels": paper.get("labels", [])
                    })
            except json.JSONDecodeError:
                print(f"Error decoding JSON in file: {json_file}")
    return venue_dict

def export_papers_to_readme(venue_dict, output_dir):
    """Creates directories for venues, saves papers as markdown files, and generates a README.md."""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    title_to_path = {}
    venue_to_path = {}

    label_set = set([])
    
    for venue, papers in venue_dict.items():
        venue_dir = os.path.join(output_dir, venue.replace('/', '_'))
        os.makedirs(venue_dir, exist_ok=True)
        
        readme_path = os.path.join(venue_dir, "README.md")
        readme_path = readme_path.replace('\\', '/')

        with open(readme_path, "w", encoding='utf8') as readme_file:
            readme_file.write(f"# {venue}\n\n")
            readme_file.write(f"Number of papers: {len(papers)}\n\n")

            readme_item_strs = []
            
            for idx, paper in enumerate(papers, start=1):
                markdown_filename = f"paper_{idx}.md"
                markdown_path = os.path.join(venue_dir, markdown_filename)
                markdown_path = markdown_path.replace('\\', '/')
                
                # Save individual paper as a markdown file
                with open(markdown_path, "w", encoding='utf8') as paper_file:
                    paper_file.write(f"# {paper['title']}\n\n")
                    paper_file.write(f"**Authors**: {paper['author']}\n\n")
                    paper_file.write(f"**Abstract**:\n\n{paper['abstract']}\n\n")
                    paper_file.write(f"**Link**: [Read Paper]({paper['url']})\n\n")

                    labels_with_links = []
                    for label in paper['labels']:
                        labels_with_links.append(f"[{label}](../../labels/{label.replace(' ', '_')}.md)")
                    paper_file.write(f"**Labels**: {', '.join(labels_with_links)}\n")
                
                readme_item_str = f"## [{paper['title']}]({markdown_filename})\n"
                readme_item_str += f"- **Authors**: {paper['author']}\n"
                readme_item_str += f"- **Abstract**: {paper['abstract'][:500]}...\n"
                readme_item_str += f"- **Link**: [Read Paper]({paper['url']})\n"
                
                labels_with_links = []
                for label in paper['labels']:
                    labels_with_links.append(f"[{label}](../../labels/{label.replace(' ', '_')}.md)")
                readme_item_str += f"- **Labels**: {', '.join(labels_with_links)}\n"

                readme_item_strs.append(readme_item_str)

                label_set = label_set.union(set(paper['labels']))

                title_to_path[paper['title']] = markdown_path
                venue_to_path[venue] = readme_path

            sorted_readme_item_strs = sorted(readme_item_strs)
            readme_file.write("\n\n".join(sorted_readme_item_strs))

    return title_to_path, venue_to_path, label_set

def get_flattened_labels(label_dict):
    flattened_labels = {}
    for label in label_dict:
        flattened_labels[label] = label_dict[label]
        flattened_labels.update(get_flattened_labels(label_dict[label]))
    return flattened_labels

def capitalize_word(s):
    if s.lower() in {"dbms", "llm", "ir", "pl"}:
        return s.upper()
    else:
        return s.capitalize()

def generate_readme_from_label(label, categories, label_to_papers, title_to_path, venue_to_path, level=1):
    capitalized_label = ' '.join([capitalize_word(word) for word in label.split()])

    content = f"{'#' * level} {capitalized_label}\n\n"

    flattened_labels = get_flattened_labels(categories)

    subcategories = flattened_labels[label]

    for sub_label in subcategories:
        content += generate_readme_from_label(sub_label, subcategories, label_to_papers, title_to_path, venue_to_path, level + 1) + "\n\n"

    paper_list = []
    if len(subcategories) == 0:
        for paper in label_to_papers[label]:
            paper_str = f"- [{paper['title']}]({title_to_path[paper['title']].replace('../data/papers/', '../')}), ([{paper['venue']}]({venue_to_path[paper['venue']].replace('../data/papers/', '../')}))\n" + "\n"
            paper_str += f"  - **Abstract**: {paper['abstract'][:500]}...\n"
            labels_with_links = []
            for label in paper['labels']:
                labels_with_links.append(f"[{label}]({label.replace(' ', '_')}.md)")
            paper_str += f"  - **Labels**: {', '.join(labels_with_links)}\n"
            paper_list.append(paper_str)

    sorted_paper_list = sorted(paper_list)
    content += "\n\n".join(sorted_paper_list)
    
    return content

def generate_readme_from_label_for_paradigm(label, categories, label_to_papers, title_to_path, venue_to_path, level=1):
    assert label in {"benchmark", "survey", "empirical study"}
    capitalized_label = ' '.join([capitalize_word(word) for word in label.split()])

    content = f"{'#' * level} {capitalized_label}\n\n"

    sublabels = set(categories.keys()) - set(["benchmark", "survey", "empirical study"])

    sub_label_items = []
    all_papers = []
    titleset = set([])
    for sub_label in label_to_papers:
        for paper in label_to_papers[sub_label]:
            if paper['title'] not in titleset:
                titleset.add(paper['title'])
                all_papers.append(paper)

    for sub_label in sorted(list(sublabels)):
        capitalized_label = ' '.join([capitalize_word(word) for word in sub_label.split()])
        single_content = f"{'#' * (level + 1)} {capitalized_label}\n\n"
        paper_strs = []
        for paper in all_papers:
            if label in paper['labels'] and sub_label in paper['labels']:
                paper_str = f"- [{paper['title']}]({title_to_path[paper['title']].replace('../data/papers/', '../')}), ([{paper['venue']}]({venue_to_path[paper['venue']].replace('../data/papers/', '../')}))\n" + "\n"
                paper_str += f"  - **Abstract**: {paper['abstract'][:500]}...\n"
                labels_with_links = []
                for sub_sub_label in paper['labels']:
                    labels_with_links.append(f"[{sub_sub_label}]({sub_sub_label.replace(' ', '_')}.md)")
                paper_str += f"  - **Labels**: {', '.join(labels_with_links)}\n"
                paper_strs.append(paper_str)
        single_content += "\n".join(sorted(paper_strs))    
        if len(paper_strs) > 0:
            sub_label_items.append(single_content)
    content += "\n".join(sorted(sub_label_items))
    return content

def get_all_labels(label_dict):
    all_labels = set([])
    for label in label_dict:
        all_labels.add(label)
        all_labels = all_labels.union(set(get_all_labels(label_dict[label])))
    return all_labels


def classify_papers_by_label(venue_dict, title_to_path, venue_to_path):
    with open('../data/category.json', 'r') as f:
        label_category = json.load(f)["categories"]

    label_to_path = {}
    labels = get_all_labels(label_category)

    label_paper_dict = {}
    for venue in venue_dict:
        for paper in venue_dict[venue]:
            for label in paper['labels']:
                if label not in labels:
                    print(paper)
                    print(label)
                    print("You use a undefined label. Please submit an issue first to apply for a taxonomy change.")
                    exit(0)
                if label not in label_paper_dict:
                    label_paper_dict[label] = []
                label_paper_dict[label].append(paper)

    output_directory = '../data/papers/labels'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for label in labels:
        if label in {"benchmark", "survey", "empirical study"}:
            readme_content = generate_readme_from_label_for_paradigm(label, label_category, label_paper_dict, title_to_path, venue_to_path)
        else:
            readme_content = generate_readme_from_label(label, label_category, label_paper_dict, title_to_path, venue_to_path)

        output_path = os.path.join(output_directory, f"{label.replace(' ', '_')}.md")
        with open(output_path, 'w', encoding='utf8') as output_file:
            output_file.write(readme_content)
            label_to_path[label] = output_path
    return label_to_path, label_paper_dict


def generate_main_readme(label_paper_dict):
    # read lines from ../data/template.txt
    with open('../data/template.txt', 'r') as f:
        lines = f.readlines()

    pattern = re.compile(r'- \[(.*?)\]\((.*?)\)\s+\(\{(c\d+)\}\)')
    matches = pattern.findall("\n".join(lines))

    readme_content = "".join(lines)
    for match in matches:
        label = match[0].lower().replace('_', ' ')
        for labeltmp in label_paper_dict:
            if label.lower() == labeltmp.lower():
                readme_content = readme_content.replace("{" + match[2] + "}", str(len(label_paper_dict[labeltmp])))

    with open('../README.md', 'w') as f:
        f.write(readme_content)


def main():
    input_directory = '../data/labeldata'
    output_directory = '../data/papers/venues'
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    
    json_files = collect_json_files(input_directory)
    venue_dict = extract_papers_by_venue(json_files)
    title_to_path, venue_to_path, label_set = export_papers_to_readme(venue_dict, output_directory)
    label_to_path, label_paper_dict = classify_papers_by_label(venue_dict, title_to_path, venue_to_path)
    generate_main_readme(label_paper_dict)


if __name__ == "__main__":
    main()
