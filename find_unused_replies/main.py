import re


def get_prompt():
    prompt_file = f"./prompt.txt"
    with open(prompt_file, "r") as f:
        return "".join(f.readlines())


if __name__ == "__main__":
    replies = ["/shake:we offer vanilla, chocolate, oreo, strawberry and our new salted caramel shakes",
              "/shake_flavor:would you like chocolate, vanilla, or strawberry?", "/hand-breaded:tenders or sandwich?",
              "/small_combo_off_menu:small combos are still available off menu.",
              "/apple_juice:i\u2019m sorry, we don\u2019t have apple juice. would you like orange juice instead?",
              "/loaded_fries:would you like el diablo or guacamole loaded fries?",
              "/burrito:would you like the sausage, bacon, loaded, or steak breakfast burrito?", "/welcome:my pleasure",
              "/value_or_double:would you like to make that a double?", "/combo:would you like to make that a combo?",
              "/order-when:order when ready please", "/burger_new:would that be a double or angus?",
              "/second-order:what would you like for the second order?", "/stars:would you like 6, or 9 stars?",
              "/wait:  ", "/bacon:would you like the western, guacamole, or double bacon cheeseburger?",
              "/desserts:we have apple pie, chocolate cake, chocolate chip cookies, and hand-scooped ice-cream shakes",
              "/correct:is your order correct?", "/size:would you like to make that a large?",
              "/coupon_items:what items are in your offer?", "/what-size:what size would you like?",
              "/sauce:what sauce would you like?", "/drink:what drink would you like?",
              "/double_burger:which double cheeseburger would you like?",
              "/special_value:11 of our craveable menu items. including our new bacon, guacamole, cali, and jalapeno junior cheeseburgers, spicy chicken sandwich, 6 piece chicken stars, small french fries, chocolate chip cookie, and chocolate cake. all for under 4 dollars",
              "/upsell-custom:Got it. would you like to try 2 apple turnovers for two twenty-nine?",
              "/total:please pull forward to the window for your total!",
              "/cancel_order:Okay. Canceled. Please order when ready", "/say-again:Could you say that again?",
              "/yes_item:yes we do have that.", "/grilled_cheese:would you like the sausage or bacon grilled cheese?",
              "/chicken:would you like the original, jalapeno, bacon swiss, club, santa fe, or the barbeque",
              "/poppers:would you like 6 or 9 jalapeno poppers?", "/anything-else:Anything else?",
              "/cinnamon_roll_86:cinnamon rolls are no longer available. may i suggest our french toast dips?",
              "/next_window:next window please",
              "/beyond_86:beyond is no longer available. may i suggest our new no meat famous or no meat el diablo?",
              "/greet:Thank you for choosing Carls Jr! What can we get started for you today?",
              "/request-window:please be sure to request that at the window",
              "/kids:which kid\u2019s meal would you like?",
              "/jalapeno_angus_86:the jalapeno angus is no longer available. may i suggest our el diablo?",
              "/original_angus_86:the original angus is no longer available. may i suggest our angus famous star?",
              "/plain:would you like that plain with or without cheese?", "/total:please proceed to window for total",
              "/sauce_options:we have buttermilk ranch, honey mustard, barbeque and buffalo",
              "/shake:what shake flavor?", "/pepsi:is coke okay?", "/tenders:would you like 3, 5, or 10 tenders?",
              "/wrap:ranch, barbeque, santa fe or diablo", "/kid_meal:which kid meal would you like?",
              "/biscuit-burrito:would you like a biscuit or burrito?",
              "/kids_options:for kids meals we have a hamburger, cheeseburger, 4 piece chicken stars, 6 piece chicken stars, and chicken tenders",
              "/delivery-order:please pull forward to the window to pick up your order.",
              "/which-cheese:would you like american, swiss or pepper jack cheese?",
              "/charbroiled:which charbroiled sandwich would you like?",
              "/hand-breaded:would you like the bacon and swiss or the original?",
              "/total:please proceed to the window for your total",
              "/kids_stars:would you like the 4 or 6 kid\u2019s star meal?"]

    discard_replies = ['/3', '/rejecting', '/4', '/describe-Famous']

    prompts = get_prompt()
    # print(prompts)
    pattern = r'/\w+[-\w]*'
    replies_in_rules = set(re.findall(pattern, prompts))
    print("replies_in_rules", replies_in_rules)
    rules_dosnot_exist_in_replies = []
    for rr in replies_in_rules:
        found = False
        for reply in replies:
            if rr in reply:
                found = True
                break
        if not found and rr not in discard_replies:
            rules_dosnot_exist_in_replies.append(rr)

    print("rules_dosnot_exist_in_replies", rules_dosnot_exist_in_replies)



