import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    dudes = df.loc[df['sex']=='Male']
    average_age_men = round(dudes['age'].mean())

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = (df['education'].value_counts().get('Bachelors')/df.shape[0])*100

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education_categories = ["Bachelors", "Masters", "Doctorate"]
    higher_education = df[df['education'].isin(higher_education_categories)]

    lower_education_categories = ['HS-grad', 'Some-college', 'Assoc-voc', '11th', 'Assoc-acdm', 
                                  '10th', '7th-8th', 'Prof- school', '9th', '12th', '5th-6th',  
                                  '1st- 4th', 'Preschool']
    lower_education = df[df['education'].isin(lower_education_categories)]

    # percentage with salary >50K
    low_salary_count = higher_education[higher_education['salary'] == '>50K'].shape[0]
    total_individuals = higher_education.shape[0]
    higher_education_rich = (low_salary_count / total_individuals) * 100

    low_salary_count = lower_education[lower_education['salary'] == '>50K'].shape[0]
    total_individuals = lower_education.shape[0]
    lower_education_rich = (low_salary_count / total_individuals) * 100

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df['hours-per-week']==1]

    rich_percentage = (num_min_workers['salary'].value_counts().get('>50K')/
                       num_min_workers.shape[0])*100

    # What country has the highest percentage of people that earn >50K?

    high_salary_data=df[df['salary']=='>50K']

    country_salary_percentages = (high_salary_data.groupby('native-country').size()/df.groupby('native-country').size()) * 100

    highest_earning_country=country_salary_percentages.idxmax()
    highest_earning_country_percentage= country_salary_percentages.max()

    # Identify the most popular occupation for those who earn >50K in India.
    india = high_salary_data[high_salary_data['native-country']=='India']
    top_IN_occupation = india['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data()