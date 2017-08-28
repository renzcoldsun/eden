tablename = "sms_inbound"

db.define_table(tablename,
    Field('message'),
    s3base.s3_date(label=T('Sent Date')),
    Field('sender'),
    Field('recipient'),
    *s3_meta_fields()
    )

s3.crud_strings[tablename] = Storage(
    title_display = T("Received SMS"),
    title_list = T("Received SMS"),
    subtitle_list = T("Received SMS"),
    msg_list_empty = T("There are no SMS in the database")
    )

