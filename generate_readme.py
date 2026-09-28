import os
import json
import urllib.request


priority = [
    "Dynamic Programming",
    "Graph",
    "Tree",
    "Binary Tree",
    "Linked List",
    "Sliding Window",
    "Two Pointers",
    "Stack",
    "Binary Search",
    "Hash Table",
    "Greedy",
    "Heap (Priority Queue)",
    "Array",
    "String",
    "Math"
]


def get_tags(slug):
    query = """
    query singleQuestionTopicTags($titleSlug: String!) {
        question(titleSlug: $titleSlug) {
            topicTags {
                name
            }
        }
    }
    """

    data = json.dumps({
        "query": query,
        "variables": {
            "titleSlug": slug
        },
        "operationName": "singleQuestionTopicTags"
    }).encode()

    request = urllib.request.Request(
        "https://leetcode.com/graphql/",
        data=data,
        headers={
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0"
        }
    )

    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read())

    return [tag["name"] for tag in result["data"]["question"]["topicTags"]]


def get_categories(tags):
    categories = []

    for category in priority:
        if category in tags:
            categories.append(category)

    if not categories:
        categories.append("Other")

    return categories


def main():
    categories = {}
    solved = set()

    for folder in os.listdir("."):
        if not os.path.isdir(folder):
            continue

        if folder.startswith("."):
            continue

        parts = folder.split("-", 1)

        if len(parts) != 2:
            continue

        number = parts[0]

        if not number.isdigit():
            continue

        slug = parts[1]
        solved.add(folder)

        try:
            tags = get_tags(slug)
            task_categories = get_categories(tags)
        except:
            task_categories = ["Other"]

        for category in task_categories:
            if category not in categories:
                categories[category] = []

            categories[category].append((int(number), folder))

    lines = []

    lines.append("# LeetCode Solutions")
    lines.append("")
    lines.append(f"Total solved: **{len(solved)}**")
    lines.append("")

    for category in priority + ["Other"]:
        if category not in categories:
            continue

        lines.append(f"## {category}")
        lines.append("")

        tasks = sorted(categories[category])

        for number, folder in tasks:
            title = folder.split("-", 1)[1].replace("-", " ").title()

            lines.append(
                f"- [{number}. {title}](./{folder})"
            )

        lines.append("")

    with open("README.md", "w") as file:
        file.write("\n".join(lines))


if __name__ == "__main__":
    main()
