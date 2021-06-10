from accesslink import AccessLink

accesslink = AccessLink(client_id="3ee72188-852b-444a-8017-028513c841ac",
                        client_secret="f814078e-54cc-49c8-91bc-ace9200f921c")

user_info = accesslink.users.get_information(user_id="3ee72188-852b-444a-8017-028513c841ac",
                                             access_token='147a1036cd23a772f06a251a35fca3db')

print(user_info)