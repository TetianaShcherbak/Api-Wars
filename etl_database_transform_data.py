from etl_database_extract_data import get_planet_database_content, get_planet_residents_amount

CONTENT_TABLE_HEADER = ['Name', 'Diameter', 'Climate', 'Terrain', 'Surface Water Percentage', 'Population', 'Residents','']


def get_predared_planet_database_content(start_row_number=0, row_amount=10):
    data = get_planet_database_content(start_row_number,row_amount)
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
