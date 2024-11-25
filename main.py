from fire import Fire
from markdownify import markdownify
import md2md


def convert(input_file: str, output_file: str = 'output.md') -> None:
    markdown_text: str = ''
    
    if input_file.endswith('.html'):
        with open(input_file, encoding='utf-8') as f:
            raw_html: str = f.read()
            markdown_text: str = markdownify(raw_html)
        
        markdown_text = markdown_text.replace(
            'ブラウザの JavaScript がオフ（ブロックまたは許可しない）に設定されているため、このページは正常に機能しません。',
            ''
        )

    elif input_file.endswith('.md'):
        with open(input_file, encoding='utf-8') as f:
            markdown_text: str = f.read()
            
    else:
        print('this file type is not supported')
        return

    markdown_text: str = md2md.convert(markdown_text)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(markdown_text)

if __name__=='__main__':
    Fire(convert)