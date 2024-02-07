import re


# Parse Provided Database Model Dump and Generate DDL
def parse_and_generate_ddl(file_path):
    def create_schema_statement(schema_name_f):
        return f"CREATE SCHEMA IF NOT EXISTS {schema_name_f};\n"

    def create_table_statement(schema_name_f, table_name_f, columns_f):
        column_definitions = ',\n   '.join(columns_f)
        # noinspection SqlNoDataSourceInspection
        return f"CREATE TABLE IF NOT EXISTS {schema_name_f}.{table_name_f} (\n    {column_definitions}\n);\n"

    with open(file_path, 'r') as file:
        content = file.read()

        schema_name_match = re.search(r'^(.*?): schema', content, re.MULTILINE)
        schema_name = schema_name_match.group(
            1) if schema_name_match else 'public'  # default schema to public if not found

        ddl_statements = [create_schema_statement(schema_name)]

        tables = re.findall(r'\n\s+(\w+): table\n(.*?)(?=\n\s*\w+: table|\Z)', content, re.DOTALL)
        for table_name, table_details in tables:
            # Filtering out non-column lines from table details
            table_details_filtered = re.sub(r'(--.*\n|\+.*\n)', '', table_details)  # Removes comments and list markers
            column_matches = re.findall(r'^\s+(\w+): (\w+)(.*?)$', table_details_filtered, re.MULTILINE)
            columns = []
            for col_name, col_type, col_details in column_matches:
                column_def = f"{col_name} {col_type.upper()}"
                if "nextval" in col_details:
                    column_def = f"{col_name} {'SERIAL' if col_type.lower() == 'integer' else 'BIGSERIAL' if col_type.lower() == 'bigint' else 'SMALLSERIAL'} NOT NULL"
                else:
                    default_val_match = re.search(r'default (.+?)(?:\s|$)', col_details)
                    if default_val_match:
                        column_def += f" DEFAULT {default_val_match.group(1)}"
                    if "NN" in col_details:
                        column_def += " NOT NULL"

                columns.append(column_def)

            ddl_statements.append(create_table_statement(schema_name, table_name, columns))

        return '\n'.join(ddl_statements)


# test input and output file paths
file_path = 'carrier_integration_dump_sample.txt'
output_file_path = 'generated_ddl.sql'

# generate DDL and write to the output file
ddl_sql = parse_and_generate_ddl(file_path)
with open(output_file_path, 'w') as output_file:
    output_file.write(ddl_sql)

print(f"DDL has been generated and saved to {output_file_path}")
