from examples.core import fictional_cost
if __name__ == '__main__':
    for input_tokens, output_tokens in ((3000,500),(1500,500),(3000,250)):
        print('Fictional total for 10000 calls:', fictional_cost(input_tokens, output_tokens)*10000)
