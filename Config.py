import shelve


class Config:

    modes = [
                {
                    'name': 'Blog',
                    'route': 'blog',
                    'add': 'admin/blog/add',
                    'enabled': True
                },
                {
                    'name': 'Forum',
                    'route': 'forum',
                    'add': 'admin/forum/add',
                    'enabled': True
                },
                {
                    'name': 'Newsfeed',
                    'route': 'newsfeed',
                    'add': 'admin/newsfeed/add',
                    'enabled': True
                },
                {
                    'name': 'Forms',
                    'route': 'forms',
                    'add': 'admin/forms/add',
                    'enabled': True
                },
                {
                    'name': 'Catalog',
                    'route': 'catalog',
                    'add': 'admin/catalog/add',
                    'enabled': True
                }
            ]
    entry_single_page = True
    article_per_page = True
    pagination_entry_per_page = 20

    def __init__(self):
        self.config_path = "db/shelve.db"
        shelve_db = shelve.open(self.config_path)

        if not shelve_db.has_key("modes"):
            shelve_db["modes"] = self.modes

        if not shelve_db.has_key('entry_single_page'):
            shelve_db["entry_single_page"] = self.entry_single_page

        if not shelve_db.has_key('pagination_entry_per_page'):
            shelve_db[
                'pagination_entry_per_page'] = self.pagination_entry_per_page

        shelve_db.close()
        self.load()

    def save(self):
        shelve_db = shelve.open(self.config_path)
        shelve_db['modes'] = self.modes

        shelve_db['pagination_entry_per_page'] = self.entry_single_page
        shelve_db['entry_single_page'] = self.entry_single_page

        shelve_db.close()

    def load(self):
        shelve_db = shelve.open(self.config_path)
        if shelve_db.has_key('modes'):
            self.modes = shelve_db['modes']

        if shelve_db.has_key('pagination_entry_per_page'):
            self.pagination_entry_per_page = shelve_db[
                'pagination_entry_per_page']

        if shelve_db.has_key('entry_single_page'):
            self.pagination_entry_per_page = shelve_db.has_key(
                'entry_single_page')

        shelve_db.close()