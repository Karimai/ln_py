def getShiftedString(s, leftShifts, rightShifts):
    if leftShifts == rightShifts: return s

    if leftShifts > rightShifts:
        leftShifts -= rightShifts
        for _ in range(leftShifts):
            s = s[1:] + s[0]
    else:
        rightShifts -= leftShifts
        for _ in range(rightShifts):
            s = s[-1] + s[0:len(s)-1]
    return s


print(getShiftedString("abcd", 1, 2) == 'dabc')

def split_into_sublists(lst):
    sublists = []
    for i in range(1, len(lst)):
        sublist1 = lst[:i]
        sublist2 = lst[i:]
        sublists.append((sublist1, sublist2))
    return sublists


def beautifulSubarrays(arr, numOdds):
    print("aa: ", arr, " odds: ", numOdds)
    subarrays = []
    n = len(arr)

    for start in range(n):
        for end in range(start + 1, n + 1):
            subarrays.append(arr[start:end])
    reslst = []
    for lst in subarrays:
        if sum(1 for i in lst if not i % 2 ) == numOdds:
            reslst.append(lst)
    return len(reslst)


print(beautifulSubarrays([2, 5, 4, 9],  1))


def calculate_score(review, positive_keywords, negative_keywords):
    score = 0
    for word in review.split():
        if word in positive_keywords:
            score += 3
        elif word in negative_keywords:
            score -= 1
    return score


def awardTopKHotels(positive_keywords, negative_keywords, hotel_ids, reviews, k):
    hotel_scores = {}

    for i in range(len(hotel_ids)):
        hotel_id = hotel_ids[i]
        review = reviews[i]
        if hotel_id not in hotel_scores:
            hotel_scores[hotel_id] = 0
        score = calculate_score(review, positive_keywords.split(), negative_keywords.split())
        hotel_scores[hotel_id] += score

    sorted_hotels = sorted(hotel_scores.items(), key=lambda x: x[1], reverse=True)

    top_k_hotels = [hotel[0] for hotel in sorted_hotels[:k]]

    return top_k_hotels


# Example usage
positive_keywords = "breakfast beach citycenter location metn31.1.11V staff price"
negative_keywords = "not"
hotel_ids = [1, 2, 1, 1, 2]
reviews = [
    "This hotel has a nice view of the citycenter. The location is perfect.",
    "The breakfast Is ok. Regarding location, it Is quite far from citycenter but price is cheap so it is worth.",
    "Location Is excellent, .5 minutes from citycenter. There is also a metro station very close to the hotel.",
    "They said I couldret take my dog and there were other guests with dogs) That is not fair.",
    "Very friendly staff and good cost-benefit ratio. Its location is a bit far from citycenter."
]
k = 2

top_hotels = awardTopKHotels(positive_keywords, negative_keywords, hotel_ids, reviews, k)
print(top_hotels)  # Output: [2, 1]

ths = awardTopKHotels('breakfast beach citycenter location metro view staff price',
                      "not",
                      [1, 2, 1, 1, 2],
                      ['This hotel has a nice view of the citycenter. The location is perfect.',
                       'The breakfast is ok. Regarding location, it is quite far from citycenter but price is cheap so it is worth.',
                       'Location is excellent, 5 minutes from citycenter. There is also a metro station very close to the hotel.',
                       "They said I couldn't take my dog and there were other guests with dogs! That is not fair.",
                       'Very friendly staff and good cost-benefit ratio. Its location is a bit far from citycenter.'],
                      2)


