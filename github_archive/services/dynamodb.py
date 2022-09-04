import boto3
import time
from boto3.dynamodb.conditions import Attr, Key


class Dynamodb:
    def __init__(self) -> None:
        self.db_client = boto3.client("dynamodb", verify=False)
        self.db_resource = boto3.resource("dynamodb", verify=False)

    def create_table(
        self,
        table_name,
        key_schema,
        attribute_definition,
        billing_mode="PAY_PER_REQUEST",
    ):
        # Attributes given in attribute_definition should be an
        # either HASH|RANGE
        # HASH---> partition key
        # Range ---> Sort key
        # Combination of HASH and RANGE is primary key

        response = self.db_client.create_table(
            AttributeDefinitions=attribute_definition,
            TableName=table_name,
            KeySchema=key_schema,
            BillingMode=billing_mode,
        )
        return response

    def delete_table(self, table_name):
        response = self.db_client.delete_table(TableName=table_name)
        return response

    def retrive_table_data_using_get(self, table_name, filter_condition):
        # Used to filter only based on key
        # and hash columns(both hash column and key column)
        # Since we are filtering based on
        #  key and hash columns we will get single record.

        response = self.db_client.get_item(TableName=table_name, Key=filter_condition)
        result = response["Item"]
        return result

    def retrive_table_data_using_scan(
        self, table_name, filter_condition, select_columnns, alias_columns
    ):
        # If we have to use filter condition in scan,
        #  Only boto3 resources should be used
        # Scan will produce 1mb of data for each API call.
        # Select default is ALL_ATTRIBUTES
        # If we use ProjectionExpression
        # then we should use select as SPECIFIC_ATTRIBUTES

        table = self.db_resource.Table(table_name)
        response = table.scan(
            TableName=table_name,
            FilterExpression=filter_condition,
            ProjectionExpression=select_columnns,
            ExpressionAttributeNames=alias_columns,
        )
        result = response["Items"]
        while "LastEvalutedKey" in response:
            response = table.scan(
                TableName=table_name,
                FilterExpression=filter_condition,
                ProjectionExpression=select_columnns,
                ExpressionAttributeNames=alias_columns,
                ExclusiveStartKey=response["LastEvalutedKey"],
            )
            result.extend(response["Items"])

        return result

    def delete_table_entry(self, table_name, delete_condition):
        # Deleting will happen only based on HASH and KEY
        # If you are not aware of the key columns valu,
        # then use scan function and select the key columns
        # Pass the above selected key columns based for loop
        #
        response = self.db_client.delete_item(
            TableName=table_name, Key=delete_condition
        )
        return response

    def write_to_table(self, table_name, write_value):
        response = self.db_client.put_item(TableName=table_name, Item=write_value)
        return response


if __name__ == "__main__":
    db_value = Dynamodb()
    """
    # Delete table
    print(db_value.delete_table("test"))

    # Wait time to drop the table
    time.sleep(10)

    # create table, While giving column attribute
    #  only hash and range column names 
    # should be given
    print(
        db_value.create_table(
            "test",
            [
                {"AttributeName": "id", "KeyType": "HASH"},
                {"AttributeName": "num", "KeyType": "RANGE"},
            ],
            [
                {"AttributeName": "id", "AttributeType": "S"},
                {"AttributeName": "num", "AttributeType": "S"},
            ],
        )
    )

    # Wait time to create the table
    time.sleep(20)

    # put_item will put only one row,
    #  so mutilple row we have to just for loop
    print(
        db_value.write_to_table(
            table_name="test",
            write_value={"id": {"S": "1"}, "num": {"S": "100"}, "date": {"N": "123"}},
        )
    )

    # Deleting the data from table
    # Pass only the key column value
    print(
        db_value.delete_table_entry(
            table_name="test", delete_condition={"id": {"S": "1"}, "num": {"S": "100"}}
        )
    )
    """

    # Reading data based on get item, Get item will
    # read based on key columns only.
    # Related to alias column name, if any of your table name
    #  contains keywords(ie connections) then # should be
    #  used before column name.
    print(
        db_value.retrive_table_data_using_get(
            table_name="test", filter_condition={"id": {"S": "1"}, "num": {"S": "100"}}
        )
    )

    # Reading data based on scan function, Attr function should be used
    # for non primary columns.
    #  For Key columns, we should use Key Function.
    print(
        db_value.retrive_table_data_using_scan(
            table_name="test",
            filter_condition=Attr("date").eq(123) & Key("id").gt(0),
            select_columnns="id,num,#date1",
            alias_columns={"#date1": "date"},
        )
    )
    time.sleep(1)
