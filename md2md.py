import re


def replace_image_links_with_alt_text(markdown_text, prefix='', suffix=''):
    '''Markdownに含まれる画像のリンクを代替テキストに置き換える

    Args:
        markdown_text: マークダウンテキスト

    Returns:
        画像のリンクが代替テキストに置換されたマークダウンテキスト
    '''
    pattern = r'!\[(.*?)\]\((.*?)\)'
    replacement = r'\1'
    return re.sub(pattern, f'{prefix}{replacement}{suffix}', markdown_text)


def remove_links_without_alt_text(markdown_text):
    '''Markdownから代替テキストのないリンクを削除する

    Args:
        markdown_text: リンクを含むマークダウンテキスト
       
    Returns:
        代替テキストのないリンクが削除されたマークダウンテキスト
   '''

    pattern = r'\[]\((.*?)\)'
    return re.sub(pattern, '', markdown_text)


def full_width_to_half_width(markdown_text):
    '''全角数字を半角数字に変換する

    Args:
        markdown_text: 変換対象のマークダウンテキスト
        
    Returns:
        全角数字が半角、全角数字が半角数字に置き換えられたマークダウンテキスト
    '''
    return re.sub('[\uff10-\uff19]', lambda m: str(int(m.group(0))), markdown_text)


def condense_blank_lines(markdown_text):
    '''マークダウンテキストから連続した空欄の行を1行にまとめる

    Args:
        markdown_text: マークダウンテキスト

    Returns:
        空白行が1行にまとめられたマークダウンテキスト
    '''

    return re.sub(r'(\n\s*){3,}\n+', '\n\n\n', markdown_text)


def convert(markdown_text):
    '''マークダウンテキストを整形する

    Args:
        markdown_text: 整形対象のマークダウンテキスト
        
    Returns:
        整形されたマークダウンテキスト
    '''
    modified_markdown_text = replace_image_links_with_alt_text(markdown_text)
    modified_markdown_text = remove_links_without_alt_text(modified_markdown_text)
    modified_markdown_text = full_width_to_half_width(modified_markdown_text)
    modified_markdown_text = condense_blank_lines(modified_markdown_text)
    return modified_markdown_text


if __name__=='__main__':
    sample_markdown_text = \
'''
これは、サンプルのマークダウンテキストです。

![タイトルA](https://)
![タイトルB](https://)
![タイトルC](https://)

これが画像のリンクを代替テキストに置き換えたテキストです。




空白が多すぎる場合は、コンパクトにまとめます。

以上。
'''
    
    modified_markdown_text = convert(sample_markdown_text)
    
    print(modified_markdown_text)
    with open('export.md', 'w') as f:
        f.write(modified_markdown_text)