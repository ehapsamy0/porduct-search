from import_export import resources
from .models import Product, ProductPrices

class ProductResource(resources.ModelResource):
    # Step 1: Define a dictionary to accumulate data across different rows
    prices_data = {}

    class Meta:
        model = Product
        exclude = ('id',)
        import_id_fields = ('part_number',)

    def before_import_row(self, row, **kwargs):
        price_columns = [col for col in row.keys() if col.startswith('price_region_')]
        prices_info = []
        for column in price_columns:
            price_value = row.pop(column,0.00)
            prices_info.append({
                'name': column.replace('price_region_', ''),
                'price': price_value,
            })

        # Step 2: Populate the dictionary with part_number as key and price information as values
        part_number = row['part_number']
        self.prices_data[part_number] = prices_info

    def after_save_instance(self, instance, using_transactions, dry_run):
        # Step 3: Use part_number to access the accumulated price information and save it
        part_number = instance.part_number
        prices_info = self.prices_data.get(part_number, [])
        print(prices_info)
        if prices_info and not dry_run:
            for price_info in prices_info:
                ProductPrices.objects.create(
                    product=instance,
                    name=price_info['name'],
                    price=price_info.get("price",0.00),
                )

        if part_number in self.prices_data:
            del self.prices_data[part_number]  # Clear the used data
