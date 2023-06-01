from copy import copy


def make_text_linked(verses: list):
    import re
    LINK_HREF = "<a class='text-sup' href='/bible/primitku/#{}'><sup><b>{}</b></sup></a>"
    linked_verses = copy(verses)
    testament = str(linked_verses[0].testament_id)
    book = str(linked_verses[0].book_id)
    chapter = str(linked_verses[0].chapter)
    for verse in linked_verses:
        tags = re.findall(r'<[а-я\d]*>', verse.text)
        for tag in tags:
            tag_shorted = tag[1:-1]
            href = ''.join([testament, book, chapter, tag_shorted])
            verse.text = verse.text.replace(tag, LINK_HREF.format(href, tag_shorted))
    return linked_verses