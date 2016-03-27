import json


columns = ['Id', 'UserId', 'Stars', 'Date', 'BusinessId'] #create required columns 
question_dataframe_file = open('yelp222.json', 'wb')
writer = csv.writer(question_dataframe_file, delimiter=',')
writer.writerow(columns)
c = 0
with open('yelp_academic_dataset_review.json') as data_file:
    for line in data_file:
        c+=1
        review = json.loads(line)
        #writer.writerow([review['review_id'], review['user_id'], review['stars'], review['date'], review['business_id'] ] )
        review.pop('text', None)
        review.pop('type', None)
        review.pop('votes', None)
        question_dataframe_file.writelines(json.dumps(review))
print c
