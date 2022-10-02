import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')
    df['ones'] = 1

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    var = df[['race', 'ones']].groupby('race').count()
    race_count = var['ones'].sort_values(ascending=False)

    # What is the average age of men?
    var = df[['sex', 'age']]
    var = var.groupby('sex').mean()
    average_age_men = round(var.loc['Male'][0], 1)

    # What is the percentage of people who have a Bachelor's degree?
    var = df[['education', 'ones']].groupby('education').count().loc['Bachelors'][0]
    tp = df.shape[0]  # total people
    percentage_bachelors = round(var / tp * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    var = df[['education', 'salary']]
    var2 = ['Bachelors', 'Masters', 'Doctorate']
    var = var.loc[var['salary'] == '>50K'].groupby('education').count()

    higher_education = var.loc[var2]
    lower_education = var.drop(var2)

    totalh = df[['education', 'salary']].groupby('education').count()
    totalh = totalh.loc[var2].sum()[0]
    totall = df[['education', 'salary']].groupby('education').count()
    totall = totall.drop(var2).sum()[0]
    var = higher_education.sum()[0]
    var2 = lower_education.sum()[0]
    var = var / totalh * 100
    var2 = var2 / totall * 100

    # percentage with salary >50K
    higher_education_rich = round(var, 1)
    lower_education_rich = round(var2, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = min(df['hours-per-week'])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df.loc[df['hours-per-week'] == min_work_hours].shape[0]
    var = df.loc[df['salary'] == '>50K'].loc[df['hours-per-week'] == min_work_hours]
    rich_percentage = var.shape[0] / num_min_workers * 100

    # What country has the highest percentage of people that earn >50K?
    var = df[['native-country', 'salary']]
    var = var.loc[var['salary'] == '>50K'].groupby('native-country').count()
    var2 = df[['native-country', 'salary']].groupby('native-country').count()
    var = round(100 * var / var2, 1).sort_values(by='salary', ascending=False)

    highest_earning_country = var.index[0]
    highest_earning_country_percentage = var.iloc[0, 0]

    # Identify the most popular occupation for those who earn >50K in India.
    var = df[['native-country', 'occupation']]
    var = var.loc[var['native-country'] == 'India']
    var = var.groupby('occupation').count()
    top_IN_occupation = var.sort_values(by='native-country', ascending=False).index[0]

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
