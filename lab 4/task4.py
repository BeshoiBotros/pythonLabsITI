import json


def product_data_transformer():
	while True:
		names_input = input("Enter product names (comma separated): ")
		prices_input = input("Enter product prices (comma separated): ")
		try:
			names = [n.strip() for n in names_input.split(",")]
			prices = [float(p.strip()) for p in prices_input.split(",")]
			if len(names) != len(prices):
				raise ValueError
			break
		except ValueError:
			print("Invalid input. Ensure names and prices match and are valid.")

	paired = zip(names, prices)
	filtered = filter(lambda x: x[1] > 0, paired)
	transformed = map(lambda x: {"product": x[0], "price": x[1], "discounted": x[1]*0.9}, filtered)

	result = list(transformed)

	with open("products.json", "w") as f:
		json.dump(result, f, indent=4)

	print("Preview:")
	print(result[:5])