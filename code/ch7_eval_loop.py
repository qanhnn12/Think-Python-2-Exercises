def eval_loop():
    while True:
        prompt = input("Enter an expression: ")
        if prompt == "done":
            break
        new_prompt = eval(prompt)
        print(new_prompt)

    # return the last evaluated expression
    print(new_prompt)


if __name__ == '__main__':
    eval_loop()