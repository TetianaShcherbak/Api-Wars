from etl_database_extract_data import get_planet_database_content

CONTENT_TABLE_HEADER = ['Name', 'Diameter', 'Climate', 'Terrain', 'Surface Water Percentage', 'Population', 'Residents','']


def get_predared_planet_database_content(start_row_number=0, row_amount=10):
    data = get_planet_database_content(start_row_number,row_amount)
    table_content = []

    for record in data:
        row_content = []
        for key, value in dict(record).items():
            if key != 'id':
                if key != 'last_update_time' :
                    row_content.append(value)
        row_content.append('?? Residents ??')
        row_content.append('Vote_button')
        table_content.append(row_content)

    return table_content

