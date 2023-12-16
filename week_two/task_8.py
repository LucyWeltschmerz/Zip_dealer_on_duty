def love_score_is(name_1, name_2):
    true_count = sum(name_1.lower().count(letter) + name_2.lower().count(letter) for letter in 'true')
    love_count = sum(name_1.lower().count(letter) + name_2.lower().count(letter) for letter in 'love')

    love_score = str(true_count) + str(love_count)
    love_score = int(love_score)

    if love_score < 10 or love_score > 90:
        print(f'Your score is {love_score}, you go together like coke and mentos')
    elif 40 <= love_score <= 50:
        print(f'Your score is {love_score}, you are alright together')
    else:
        print(f'Your score is {love_score}')


love_score_is("Angela Yu", "Jack Bauer")
