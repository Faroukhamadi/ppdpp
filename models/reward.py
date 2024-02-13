from dotenv import load_dotenv

load_dotenv()


class RewardModel:
    def __init__(self, deal_price, seller_target_price, buyer_target_price):
        self.deal_price = deal_price
        self.seller_target_price = seller_target_price
        self.buyer_target_price = buyer_target_price

    def prompt(self, text=None):
        return text if text else "Have they reached a deal?"

    def reward(self):
        return (self.deal_price - self.seller_target_price) / (self.buyer_target_price - self.seller_target_price)


reward = RewardModel(None, None, None)

print(reward.prompt())

# Mr(.) we're using this to transform verbal feedback to scalar rewards
