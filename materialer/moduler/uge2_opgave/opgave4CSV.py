import csv

def read_reviews():
    filename = 'reviews.csv'

    with open(filename, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        print("--- Alle Reviews ---")
        for row in reader:
            print(row['review'])

def read_specific_review(target_id):
    filename = 'reviews.csv'

    with open(filename, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)

        print(f"\n--- REVIEWS FOR VISIT_ID {target_id} ---")
        for row in reader:

            if row['visit_id'] == str(target_id):
                print(f"ID: {row['visit_id']} - Review: {row['review']}")

if __name__ == '__main__':
    read_specific_review(3267)