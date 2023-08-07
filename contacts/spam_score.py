from .models import SpamDatabase


def calculate_spam_score(phone_number):
    spam_queryset = SpamDatabase.objects.all()
    spam_score = 0
    
    spam_database_phone = spam_queryset.filter(spam_phone__isnull=False)
    for spam_obj in spam_database_phone:
        if phone_number == spam_obj.spam_phone:
            spam_score += 50
            break
    
    # suspicious_patterns = ["123456", "999", "666"]
    # for pattern in suspicious_patterns:
    #     if pattern in phone_number:
    #         spam_score += 20
    
    spam_countries = spam_queryset.filter(spam_countries_code__isnull=False)
    if any(phone_number.startswith(spam_obj.spam_countries_code) for spam_obj in spam_countries):
        spam_score += 25

    if len(phone_number) > 15:
        spam_score += 50
    
    return spam_score

# # Test the function
# phone_number1 = "5555555555"
# phone_number2 = "1234567890"
# phone_number3 = "123456789"

# score1 = calculate_spam_score(phone_number1)
# score2 = calculate_spam_score(phone_number2)
# score3 = calculate_spam_score(phone_number3)

# print(f"Spam score for {phone_number1}: {score1}")
# print(f"Spam score for {phone_number2}: {score2}")
# print(f"Spam score for {phone_number3}: {score3}")
