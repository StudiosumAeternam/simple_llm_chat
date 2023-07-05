from model import generate_response
from logging import setup_logging, get_logger

setup_logging()
logger = get_logger(__name__)

def main():
    while True:
        input_text = input("You: ")
        response = generate_response(input_text).to(device)
        logger.info(f"User input: {input_text}")
        logger.info(f"GPT-Neo response: {response}")
        print("GPT-Neo: ", response)

if __name__ == "__main__":
    main()
