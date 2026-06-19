import json
import datetime


def load_site_data():
    return {
        "name": "乐鱼体育",
        "url": "https://m-site-leyu.com.cn",
        "keywords": ["乐鱼体育", "体育赛事", "在线娱乐", "综合体育平台"],
        "description": "乐鱼体育是一个综合性体育赛事娱乐平台，涵盖多种体育项目与实时资讯。",
        "tags": ["体育", "娱乐", "赛事", "资讯"],
        "version": "1.0",
        "created": "2025-03-23"
    }


def extract_summary(data: dict) -> dict:
    summary = {
        "title": data.get("name", ""),
        "url": data.get("url", ""),
        "keywords": data.get("keywords", []),
        "tags": data.get("tags", []),
        "brief": data.get("description", "")
    }
    return summary


def format_summary_line(label: str, value) -> str:
    if isinstance(value, list):
        value_str = ", ".join(value)
    else:
        value_str = str(value)
    return f"{label}: {value_str}"


def generate_formatted_output(summary: dict) -> str:
    lines = []
    lines.append("=" * 50)
    lines.append("        站点结构化摘要")
    lines.append("=" * 50)
    lines.append(format_summary_line("站点名称", summary.get("title", "")))
    lines.append(format_summary_line("访问地址", summary.get("url", "")))
    lines.append(format_summary_line("核心关键词", summary.get("keywords", [])))
    lines.append(format_summary_line("内容标签", summary.get("tags", [])))
    lines.append(format_summary_line("简短说明", summary.get("brief", "")))
    lines.append("-" * 50)
    lines.append(f"生成时间: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 50)
    return "\n".join(lines)


def save_summary_to_file(summary: dict, filepath: str = "site_summary_output.txt"):
    output = generate_formatted_output(summary)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(output)
    return filepath


def display_summary(summary: dict):
    print(generate_formatted_output(summary))


def main():
    site_data = load_site_data()
    summary = extract_summary(site_data)
    display_summary(summary)
    saved_path = save_summary_to_file(summary)
    print(f"\n摘要已保存至: {saved_path}")


if __name__ == "__main__":
    main()