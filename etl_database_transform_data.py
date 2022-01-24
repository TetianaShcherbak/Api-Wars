from etl_database_extract_data import get_planet_database_content, get_planet_residents_amount, get_planet_residents_data

CONTENT_TABLE_HEADER = ['Name', 'Diameter', 'Climate', 'Terrain', 'Surface Water Percentage', 'Population', 'Residents','']
CONTENT_RESIDENTS_TABLE_HEADER = ['Name', 'Height', 'Mass', 'Skin color', 'Hair color', 'Eye color', 'Birth year', 'Gender']


def get_prepared_planet_database_content(page_number=1, row_amount=10):
    start_row_number = int(page_number) * 10 - 10
    data = get_planet_database_content(start_row_number, row_amount)
    table_content = []

    for record in data:
        row_content = []
        prepared_residents_amount = 0
        for key, value in dict(record).items():
            if key == 'name':
                prepared_residents_amount = get_prepared_residents_amount(value)
            if key != 'id':
                if key != 'last_update_time':
                    row_content.append(value)

        row_content.append(prepared_residents_amount)
        row_content.append('Vote_button')
        table_content.append(row_content)

    return table_content


def get_prepared_residents_amount(planet):
    residents_amount = get_planet_residents_amount(planet)
    prepared_residents_amount = str(residents_amount) + ' resident(s)'
    if residents_amount is None:
        prepared_residents_amount = 'No known residents'

    return prepared_residents_amount


def get_prepared_planet_residents_content(planet):
    data = get_planet_residents_data(planet)
    residents_table_content = []

    for record in data:
        row_content = []

        for key, value in dict(record).items():
            if key != 'id':
                if key != 'last_update_time':
                    if key != 'planet_name':
                        row_content.append(value)

        residents_table_content.append(row_content)

    return residents_table_content