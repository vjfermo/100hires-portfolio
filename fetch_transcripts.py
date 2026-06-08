"""
YouTube Transcript Fetcher v2 - 100Hires Portfolio Project
Topic: AI-Powered SEO Content Production
Updated for youtube-transcript-api v1.x
"""

from youtube_transcript_api import YouTubeTranscriptApi
import os
import re

VIDEOS = [
    (
        "https://www.youtube.com/watch?v=D7LBx8RFOcQ",
        "Ryan Law",
        "AI Writing at Scale - Ahrefs Step-by-Step Workflow",
        "Documents the actual AI content production workflow Ahrefs used internally to publish at scale with ranked results"
    ),
    (
        "https://www.youtube.com/watch?v=iVZrVeESnFQ",
        "Ryan Law",
        "How to Automate Blog Writing with AI - Keyword to Published",
        "Step-by-step automation of AI content pipeline from keyword research through publishing"
    ),
    (
        "https://www.youtube.com/watch?v=mL1W1SMtTT4",
        "Ryan Law",
        "How to Win in AI Search - Real Data No Hype",
        "Data-backed research on Answer Engine Optimization and what content types AI prefers to cite"
    ),
    (
        "https://www.youtube.com/watch?v=jQXvbeYF5go",
        "Kevin Indig",
        "Google Will Kill Your Traffic - Here Is How You Adapt",
        "Research-backed analysis of how AI Overviews are restructuring organic traffic and what content strategy adapts"
    ),
    (
        "https://www.youtube.com/watch?v=NCbgNMbpDCY",
        "Kevin Indig",
        "AI Overview Impact on SEO - AirOps Webinar",
        "Practical walkthrough of AI Overviews impact with guidance on content production that still drives results"
    ),
    (
        "https://www.youtube.com/watch?v=mgI1U7XPsUA",
        "Lily Ray",
        "How SEO Is Evolving in 2025 - AI Reddit and Ranking",
        "Data-driven analysis of what builds ranking authority in AI-influenced search, including authenticity signals"
    ),
    (
        "https://www.youtube.com/watch?v=wLjTTlG3oNk",
        "Chima Mmeje",
        "How To Start Using AI Content In Your Marketing",
        "Practical framework for integrating AI content tools responsibly into a content marketing workflow"
    ),
    (
        "https://www.youtube.com/watch?v=8-PS7gR2G0I",
        "Ross Hudgens",
        "AI Visibility Data Journalism and the Future of SEO",
        "Agency-level analysis of how AI is reshaping content production and visibility measurement for brands"
    ),
]


def get_video_id(url):
    patterns = [
        r'(?:v=)([^&\n?#]+)',
        r'(?:youtu\.be/)([^&\n?#]+)',
        r'(?:embed/)([^&\n?#]+)',
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None


def sanitize_filename(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    text = re.sub(r'\s+', '-', text.strip())
    text = re.sub(r'-+', '-', text)
    return text[:80]


def format_transcript(raw_transcript):
    lines = []
    current_paragraph = []
    for i, entry in enumerate(raw_transcript):
        # Handle both v0.x dict format and v1.x object format
        if hasattr(entry, 'text'):
            text = entry.text.strip()
        else:
            text = entry.get('text', '').strip()
        if not text or text in ('[Music]', '[Applause]'):
            continue
        current_paragraph.append(text)
        if len(current_paragraph) >= 15:
            lines.append(' '.join(current_paragraph))
            current_paragraph = []
    if current_paragraph:
        lines.append(' '.join(current_paragraph))
    return '\n\n'.join(lines)


def save_transcript(url, author, title, reason):
    video_id = get_video_id(url)
    if not video_id:
        print(f"  ERROR: Could not extract video ID from {url}")
        return False

    folder_name = sanitize_filename(title)
    dir_path = os.path.join('research', 'youtube-transcripts', folder_name)
    os.makedirs(dir_path, exist_ok=True)
    filepath = os.path.join(dir_path, 'transcript.md')

    if os.path.exists(filepath):
        print(f"  SKIP: Already exists - {title}")
        return True

    try:
        api = YouTubeTranscriptApi()
        raw = api.fetch(video_id)
        transcript_text = format_transcript(raw)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n")
            f.write(f"**Author:** {author}  \n")
            f.write(f"**URL:** {url}  \n")
            f.write(f"**Video ID:** {video_id}  \n")
            f.write(f"**Why collected:** {reason}  \n\n")
            f.write(f"---\n\n")
            f.write(f"## Transcript\n\n")
            f.write(transcript_text)

        word_count = len(transcript_text.split())
        print(f"  SAVED: {title} ({word_count:,} words)")
        return True

    except Exception as e:
        print(f"  ERROR: {type(e).__name__} - {title}: {str(e)[:100]}")
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n")
            f.write(f"**Author:** {author}  \n")
            f.write(f"**URL:** {url}  \n")
            f.write(f"**Note:** Could not fetch transcript automatically: {type(e).__name__}\n")
        return False


def main():
    print("=" * 60)
    print("YouTube Transcript Fetcher v2")
    print("100Hires Portfolio - AI-Powered SEO Content Production")
    print("=" * 60)
    print()

    os.makedirs(os.path.join('research', 'youtube-transcripts'), exist_ok=True)

    success = 0
    failed = 0

    for url, author, title, reason in VIDEOS:
        print(f"Processing: {author} - {title[:50]}...")
        result = save_transcript(url, author, title, reason)
        if result:
            success += 1
        else:
            failed += 1
        print()

    print("=" * 60)
    print(f"Done. Saved: {success} | Failed/Skipped: {failed}")
    print(f"Files saved to: research/youtube-transcripts/")
    print("=" * 60)


if __name__ == "__main__":
    main()