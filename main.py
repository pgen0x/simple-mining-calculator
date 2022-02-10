import sys
import requests

# ASCII color codes
YELLOW = '\033[33m'
RED = '\033[31m'
END = '\033[0m'


def estimate(device_hash_rate, coin="BTC"):
	block_reward = int(requests.get(url="https://blockchain.info/q/bcperblock").json())
	difficulty = int(requests.get(url="https://blockchain.info/q/getdifficulty").json())

	# (device_hash_rate * block_reward * 86400) / (difficulty * 2 ** 32) #Ini Rumus nya
	return float(device_hash_rate * block_reward * 86400) / (difficulty * 2 ** 32)

def main():
	while True:
		sys.stdout.write(''.join(["What is your device's hash rate (in TH/s)? ", YELLOW]))

		try:
			exchange_rate = int(requests.get(url="https://blockchain.info/q/24hrprice").json())
			device_hash_rate = int(input()) * 1000000000000  # Di Convert ke H/s 1 TH/s = 1000000000000 H/s
			result = estimate(device_hash_rate)
			resultusd = result * exchange_rate
			resultperbulan = estimate(device_hash_rate) * 30
			resultusdperbulan = resultperbulan * exchange_rate

			print("{:.8f}".format(result), "BTC / Day -", "{:.2f}".format(resultusd), "USD")
			print("{:.8f}".format(resultperbulan), "BTC / Month -", "{:.2f}".format(resultusdperbulan), "USD")

			return
		except ValueError:
			sys.stdout.write(''.join([END, RED, "Please input an integer.\n\n", END]))


if __name__ == "__main__":
	main()