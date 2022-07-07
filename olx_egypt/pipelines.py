# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

from olx_egypt.models import Olx_Eg, session


class OlxEgPipeline:
    def __init__(self):
        """
        Initializes database connection and sessionmaker.
        Creates items table.
        """
        # engine = db_connect()
        # create_items_table(engine)
        # self.Session = sessionmaker(bind=engine)

    def process_item(self, item, spider):
        """
        Process the item and store to database.
        """
        # session = self.Session()
        instance = session.query(Olx_Eg).filter_by(Reference=item["Reference"]).first()
        if instance:
            return instance
        else:
            olx_item = Olx_Eg(**item)
            session.add(olx_item)

        try:
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

        return item
