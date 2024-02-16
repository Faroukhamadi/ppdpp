class RewardModel:
    USER_PROMPT = """
        Please decide whether the Buyer and the Seller have reached a deal
        at the end of the conversation. If they have reached a deal, please
        extract the deal price as [price]. You can only reply with one of
        the following sentences: They have reached a deal at [price].
        They have not reached a deal.
    """
    SYSTEM_PROMPT = """
        Given a conversation between a Buyer and a Seller, please decide
        whether the Buyer and the Seller have reached a deal at the end
        of the conversation.
    """

    def __init__(self):
        self.sample_times = 10
        self.temperature = 1.1

    def prompt(self, text=None, type="user"):
        if type == "user":
            return text if text else self.USER_PROMPT
        elif type == "system":
            return self.SYSTEM_PROMPT

    def reward(self, deal_price, seller_price, buyer_price):
        print("inside reward function")
        if deal_price is None:
            print("returning -1")
            return -1
        return (deal_price - seller_price) / (buyer_price - seller_price)


model = RewardModel()

examples = {
    "They have not reached a deal.": -1,
    "They have reached a deal at 15.": 15,
}

for example in examples:
    scalar_reward = model.reward(examples[example], 10, 20)
    print(f"Example: {example}, Scalar Reward: {scalar_reward}")
