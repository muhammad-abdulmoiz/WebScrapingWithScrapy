from scrapy.exceptions import DropItem


class AuthorPipeline:
    @staticmethod
    def process_item(item):
        # Truncate the name to 10 characters
        if 'name' in item:
            item['name'] = item['name'][:10]

        # Truncate the bio to 100 characters
        if 'bio' in item:
            item['bio'] = item['bio'][:100]

        print(f"Author: {item['name']}")
        print(f"Birthdate: {item['birthdate']}")
        print(f"Bio: {item['bio']}")
        return item


class QuotePipeline:
    def __init__(self):
        self.seen = set()

    def process_item(self, item):
        identifier = (item.get('text'), item.get('author'))
        if identifier in self.seen:
            raise DropItem(f"Duplicate item found: {item}")
        self.seen.add(identifier)

        # Get all tags and limit to 3
        tags = item.get('tags', '').split(', ')
        if len(tags) > 3:
            tags = tags[:3]
        elif len(tags) == 0:
            raise DropItem(f"Item has no tags: {item}")

        item['tags'] = ', '.join(tags)

        return item
