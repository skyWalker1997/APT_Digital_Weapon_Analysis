import os
import pickle
import json
import numpy

from Analysis.Path_Info import root_dir,result_dir,DS_strore_command

val = os.system('DS_strore_command')
dirs = os.listdir(root_dir)
dirs.sort()
APT_list = dirs

def APT_Json_Count():
    '''已有数据中APT对应的样本数量，返回列表 '''

    APT_Json_Count_list = []
    for APT in APT_list:
        temp_dir = root_dir+'/'+APT
        temp_json_file_list = os.listdir(temp_dir)
        temp_count = len(temp_json_file_list)
        APT_Json_Count_list.append(temp_count)
    return APT_Json_Count_list


def APT_Json_Count_Dict():
    '''已有数据中APT对应的样本数量，返回字典'''
    APT_Json_Count_list = APT_Json_Count()
    APT_Json_Count_dict = {}
    for i in range(0,len(APT_list)):
        APT_Json_Count_dict.update({APT_list[i]:APT_Json_Count_list[i]})
    return APT_Json_Count_dict


def APT_Json_Count_Sort():
    APT_Json_Count_dict =  APT_Json_Count_Dict()
    APT_Json_Count_dict_sorted = sorted(APT_Json_Count_dict.items(), key=lambda APT_Json_Count_dict: APT_Json_Count_dict[1], reverse=True)
    return APT_Json_Count_dict_sorted


def APT_Related_URL():
    APT_Related_URL_dict = {}
    for APT in APT_list:
        temp_dir = root_dir+'/'+APT
        json_files = os.listdir(temp_dir)
        temp_json_url_dict = {}
        for json_file in json_files:
            with open(temp_dir+'/'+json_file, 'r') as load_f:
                temp_json = json.load(load_f)
            temp_keys = temp_json.keys()
            if not 'additional_info' in temp_keys:
                temp_json_url_dict.update({json_file: []})
                continue
            temp_additional_info = temp_json['additional_info']
            temp_keys = temp_additional_info.keys()
            if not 'contacted_urls' in temp_keys:
                temp_json_url_dict.update({json_file: []})
            else:
                temp_url_list = temp_additional_info['contacted_urls']
                temp_json_url_dict.update({json_file:temp_url_list})
        APT_Related_URL_dict.update({APT:temp_json_url_dict})
    return APT_Related_URL_dict


def APT_Related_URL_Sort():
    APT_Related_URL_dict_sorted = {}
    APT_Related_URL_dict = Load_Result('APT_Related_URL_dict')
    for APT in APT_list:
        temp_APT_dict = APT_Related_URL_dict[APT]
        temp_keys = temp_APT_dict.keys()
        APT_URL_count = 0
        for key in temp_keys:
            temp_URL_count = len(temp_APT_dict[key])
            APT_URL_count = APT_URL_count + temp_URL_count
        APT_Related_URL_dict_sorted.update({APT:APT_URL_count})
    APT_Related_URL_Sort_dict = sorted(APT_Related_URL_dict_sorted.items(),key=lambda APT_Related_URL_Sort_dict: APT_Related_URL_Sort_dict[1], reverse=True)
    return APT_Related_URL_Sort_dict


def APT_Related_Domain():
    APT_Related_Domain_dict = {}
    for APT in APT_list:
        temp_dir = root_dir+'/'+APT
        json_files = os.listdir(temp_dir)
        temp_json_domain_dict = {}
        for json_file in json_files:
            with open(temp_dir+'/'+json_file, 'r') as load_f:
                temp_json = json.load(load_f)
            temp_keys = temp_json.keys()
            if not 'additional_info' in temp_keys:
                temp_json_domain_dict.update({json_file: []})
                continue
            temp_additional_info = temp_json['additional_info']
            temp_keys = temp_additional_info.keys()
            if not 'contacted_domains' in temp_keys:
                temp_json_domain_dict.update({json_file: []})
            else:
                temp_domain_list = temp_additional_info['contacted_domains']
                temp_json_domain_dict.update({json_file:temp_domain_list})
        APT_Related_Domain_dict.update({APT: temp_json_domain_dict})
    return APT_Related_Domain_dict


def APT_Related_Domain_Sort():
    APT_Related_Domain_dict_sorted = {}
    APT_Related_Domain_dict = Load_Result('APT_Related_Domain_dict')
    for APT in APT_list:
        temp_APT_dict = APT_Related_Domain_dict[APT]
        temp_keys = temp_APT_dict.keys()
        APT_Domain_count = 0
        for key in temp_keys:
            temp_Domain_count = len(temp_APT_dict[key])
            APT_Domain_count = APT_Domain_count + temp_Domain_count
        APT_Related_Domain_dict_sorted.update({APT:APT_Domain_count})
    APT_Related_Domain_Sort_dict = sorted(APT_Related_Domain_dict_sorted.items(),key=lambda APT_Related_Domain_Sort_dict: APT_Related_Domain_Sort_dict[1], reverse=True)
    return APT_Related_Domain_Sort_dict


def APT_Related_URL_Sort_By_File():
    APT_Related_URL_File_dict_sorted = {}
    APT_Related_URL_dict = Load_Result('APT_Related_URL_dict')
    for APT in APT_list:
        temp_APT_dict = APT_Related_URL_dict[APT]
        temp_keys = temp_APT_dict.keys()
        for key in temp_keys:
            temp_URL_count = len(temp_APT_dict[key])
            APT_Related_URL_File_dict_sorted.update({key:(temp_URL_count,APT)})
    print(APT_Related_URL_File_dict_sorted)
    APT_Related_URL_File_dict_sorted = sorted(APT_Related_URL_File_dict_sorted.items(),
                                       key=lambda APT_Related_URL_File_dict_sorted: APT_Related_URL_File_dict_sorted[1], reverse=True)
    return APT_Related_URL_File_dict_sorted


def APT_Related_Domain_Sort_By_File():
    APT_Related_Domain_File_dict_sorted = {}
    APT_Related_Domain_dict = Load_Result('APT_Related_Domain_dict')
    for APT in APT_list:
        temp_APT_dict = APT_Related_Domain_dict[APT]
        temp_keys = temp_APT_dict.keys()
        for key in temp_keys:
            temp_Domain_count = len(temp_APT_dict[key])
            APT_Related_Domain_File_dict_sorted.update({key:(temp_Domain_count,APT)})
    print(APT_Related_Domain_File_dict_sorted)
    APT_Related_Domain_File_dict_sorted = sorted(APT_Related_Domain_File_dict_sorted.items(),
                                       key=lambda APT_Related_Domain_File_dict_sorted: APT_Related_Domain_File_dict_sorted[1], reverse=True)
    return APT_Related_Domain_File_dict_sorted


def Sample_Behaviour_list():
    APT_Behaviour_list = []
    for APT in APT_list:
        temp_dir = root_dir + '/' + APT
        json_files = os.listdir(temp_dir)
        for json_file in json_files:
            with open(temp_dir+'/'+json_file, 'r') as load_f:
                temp_json = json.load(load_f)
            temp_keys = temp_json.keys()
            if not 'additional_info' in temp_keys:
               continue
            temp_additional_info = temp_json['additional_info']
            temp_keys = temp_additional_info.keys()
            if not 'behaviour-v1' in temp_keys:
                continue
            else:
                temp_behaviour_dict = temp_additional_info['behaviour-v1']
                temp_behaviour_keys = temp_behaviour_dict.keys()
                temp_behaviour_keys_list = tuple_to_list(temp_behaviour_keys)
                APT_Behaviour_list.extend(temp_behaviour_keys_list)
                APT_Behaviour_list = list(set(APT_Behaviour_list))
    return APT_Behaviour_list


def APT_Behaviour_Hooking_dict_sort_by_file():
    Behaviour_Hooking_dict = {}
    for APT in APT_list:
        temp_dir = root_dir + '/' + APT
        json_files = os.listdir(temp_dir)
        temp_hooking_dict = {}
        Behaviour_Hooking_dict.update({APT:{}})
        for json_file in json_files:
            with open(temp_dir + '/' + json_file, 'r') as load_f:
                temp_json = json.load(load_f)
            temp_keys = temp_json.keys()
            if not 'additional_info' in temp_keys:
                # temp_hooking_dict.update({json_file:[]})
                continue
            temp_additional_info = temp_json['additional_info']
            temp_keys = temp_additional_info.keys()
            if not 'behaviour-v1' in temp_keys:
                # temp_hooking_dict.update({json_file:[]})
                continue
            else:
                temp_behaviour_dict = temp_additional_info['behaviour-v1']
                temp_behaviour_keys = temp_behaviour_dict.keys()
                temp_behaviour_keys_list = tuple_to_list(temp_behaviour_keys)
                if not 'hooking' in temp_behaviour_keys_list:
                    # temp_hooking_dict.update({json_file:[]})
                    continue
                else:
                    temp_file_hooking_list = temp_behaviour_dict['hooking']
                    if len(temp_file_hooking_list) != 0:
                        temp_hooking_dict.update({json_file:temp_file_hooking_list})
                    else:
                        continue
            Behaviour_Hooking_dict.update({APT:temp_hooking_dict})
        print(APT,Behaviour_Hooking_dict)
        if len(Behaviour_Hooking_dict[APT]) != 0:
            print(Behaviour_Hooking_dict[APT])
    return Behaviour_Hooking_dict


def APT_Behaviour_Hooking_dict_sort_by_APT():
    APT_Behaviour_Hooking_dict = {}
    Behaviour_Hooking_dict = Load_Result('Behaviour_Hooking_dict')
    for APT in APT_list:
        temp_file_behaviour_list = Behaviour_Hooking_dict[APT]
        temp_file_hash_list = temp_file_behaviour_list.keys()
        temp_file_hash_list = tuple_to_list(temp_file_hash_list)
        temp_hooking_list = []
        for file in temp_file_hash_list:
            temp_hooking_list.append(temp_file_behaviour_list[file])
        temp_hooking_list = two_d_list_de_duplication(temp_hooking_list)
        APT_Behaviour_Hooking_dict.update({APT:temp_hooking_list})
    return APT_Behaviour_Hooking_dict


def APT_Behaviour_Network_dict_sort_by_file():
    Behaviour_Network_dict = {}
    for APT in APT_list:
        temp_dir = root_dir + '/' + APT
        json_files = os.listdir(temp_dir)
        temp_network_dict = {}
        Behaviour_Network_dict.update({APT:{}})
        for json_file in json_files:
            with open(temp_dir + '/' + json_file, 'r') as load_f:
                temp_json = json.load(load_f)
            temp_keys = temp_json.keys()
            if not 'additional_info' in temp_keys:
                continue
            temp_additional_info = temp_json['additional_info']
            temp_keys = temp_additional_info.keys()
            if not 'behaviour-v1' in temp_keys:
                continue
            else:
                temp_behaviour_dict = temp_additional_info['behaviour-v1']
                temp_behaviour_keys = temp_behaviour_dict.keys()
                temp_behaviour_keys_list = tuple_to_list(temp_behaviour_keys)
                if not 'network' in temp_behaviour_keys_list:
                    continue
                else:
                    temp_file_network_dict = temp_behaviour_dict['network']
                    temp_network_keys = temp_file_network_dict.keys()
                    temp_pop_key_list = []
                    for key in temp_network_keys:
                        if len(temp_file_network_dict[key]) == 0:
                            temp_pop_key_list.append(key)
                    for key in temp_pop_key_list:
                        temp_file_network_dict.pop(key)
                    if len(temp_file_network_dict) == 0:
                        continue
                    else:
                        temp_network_dict.update({json_file:temp_file_network_dict})
        Behaviour_Network_dict.update({APT:temp_network_dict})
        print(APT,Behaviour_Network_dict)
        if len(Behaviour_Network_dict[APT]) != 0:
            print(Behaviour_Network_dict[APT])
    return Behaviour_Network_dict


def APT_Network_Network_dict_sort_by_APT():
    Behaviour_Network_dict_sort_by_APT = {}
    Behaviour_Network_dict = Load_Result('Behaviour_Network_dict')
    for APT in APT_list:
        file_network_dict = Behaviour_Network_dict[APT]
        file_list = file_network_dict.keys()
        if len(file_list) == 0:
            Behaviour_Network_dict_sort_by_APT.update({APT:{'udp':[],'http':[],'tcp':[],'dns':[]}})
        temp_udp = []
        temp_http = []
        temp_tcp = []
        temp_dns = []
        for file in file_list:
            temp_file_network_behaviour = file_network_dict[file]
            temp_keys = temp_file_network_behaviour.keys()
            for key in temp_keys:
                if key == 'udp':
                    temp_udp.extend(temp_file_network_behaviour[key])
                if key == 'http':
                    temp_http.extend(temp_file_network_behaviour[key])
                if key == 'tcp':
                    temp_tcp.extend(temp_file_network_behaviour[key])
                if key ==  'dns':
                    temp_dns.extend(temp_file_network_behaviour[key])
        temp_udp = list(set(temp_udp))
        temp_http = DeleteDuplicate(temp_http)
        # temp_http = list(set(temp_http))
        temp_tcp = list(set(temp_tcp))
        temp_dns = DeleteDuplicate(temp_dns)
        # temp_dns = list(set(temp_dns))
        Behaviour_Network_dict_sort_by_APT.update({APT:{'udp':temp_udp,'http':temp_http,'tcp':temp_tcp,'dns':temp_dns}})
    return Behaviour_Network_dict_sort_by_APT


def APT_Behaviour_Service_dict_sort_by_file():
    Behaviour_Service_dict = {}
    for APT in APT_list:
        temp_dir = root_dir + '/' + APT
        json_files = os.listdir(temp_dir)
        temp_service_dict = {}
        Behaviour_Service_dict.update({APT:{}})
        for json_file in json_files:
            with open(temp_dir + '/' + json_file, 'r') as load_f:
                temp_json = json.load(load_f)
            temp_keys = temp_json.keys()
            if not 'additional_info' in temp_keys:
                continue
            temp_additional_info = temp_json['additional_info']
            temp_keys = temp_additional_info.keys()
            if not 'behaviour-v1' in temp_keys:
                continue
            else:
                temp_behaviour_dict = temp_additional_info['behaviour-v1']
                temp_behaviour_keys = temp_behaviour_dict.keys()
                temp_behaviour_keys_list = tuple_to_list(temp_behaviour_keys)
                if not 'service' in temp_behaviour_keys_list:
                    continue
                else:
                    temp_file_service_dict = temp_behaviour_dict['service']
                    temp_service_keys = temp_file_service_dict.keys()
                    temp_pop_key_list = []
                    for key in temp_service_keys:
                        if len(temp_file_service_dict[key]) == 0:
                            temp_pop_key_list.append(key)
                    for key in temp_pop_key_list:
                        temp_file_service_dict.pop(key)
                    if len(temp_file_service_dict) == 0:
                        continue
                    else:
                        temp_service_dict.update({json_file:temp_file_service_dict})
        Behaviour_Service_dict.update({APT:temp_service_dict})
        print(APT,Behaviour_Service_dict)
        if len(Behaviour_Service_dict[APT]) != 0:
            print(Behaviour_Service_dict[APT])
    return Behaviour_Service_dict


def APT_Behaviour_Service_dict_sort_by_APT():
    Behaviour_Service_dict_sort_by_APT = {}
    Behaviour_Service_dict = Load_Result('Behaviour_Service_dict_sort_by_file')
    for APT in APT_list:
        file_service_dict = Behaviour_Service_dict[APT]
        file_list = file_service_dict.keys()
        if len(file_list) == 0:
            Behaviour_Service_dict_sort_by_APT.update({APT: {'opened': [], 'opened-managers': []}})
        temp_opened = []
        temp_opened_managers = []
        for file in file_list:
            temp_file_service_behaviour = file_service_dict[file]
            temp_keys = temp_file_service_behaviour.keys()
            for key in temp_keys:
                if key == 'opened':
                    temp_opened.extend(temp_file_service_behaviour[key])
                if key == 'opened-managers':
                    temp_opened_managers.extend(temp_file_service_behaviour[key])

        temp_opened = DeleteDuplicate(temp_opened)
        temp_opened_managers = DeleteDuplicate(temp_opened_managers)
        Behaviour_Service_dict_sort_by_APT.update({APT: {'opened': temp_opened, 'opened_managers': temp_opened_managers}})
    return Behaviour_Service_dict_sort_by_APT


def APT_Behaviour_Extra_dict_sort_by_file():
    Behaviour_Extra_dict = {}
    for APT in APT_list:
        temp_dir = root_dir + '/' + APT
        json_files = os.listdir(temp_dir)
        temp_extra_dict = {}
        Behaviour_Extra_dict.update({APT: {}})
        for json_file in json_files:
            with open(temp_dir + '/' + json_file, 'r') as load_f:
                temp_json = json.load(load_f)
            temp_keys = temp_json.keys()
            if not 'additional_info' in temp_keys:
                continue
            temp_additional_info = temp_json['additional_info']
            temp_keys = temp_additional_info.keys()
            if not 'behaviour-v1' in temp_keys:
                continue
            else:
                temp_behaviour_dict = temp_additional_info['behaviour-v1']
                temp_behaviour_keys = temp_behaviour_dict.keys()
                temp_behaviour_keys_list = tuple_to_list(temp_behaviour_keys)
                if not 'extra' in temp_behaviour_keys_list:
                    continue
                else:
                    temp_file_extra_list = temp_behaviour_dict['extra']
                    if len(temp_file_extra_list) == 0:
                        continue
                    temp_extra_dict.update({json_file:temp_file_extra_list})
        Behaviour_Extra_dict.update({APT:temp_extra_dict})
    return Behaviour_Extra_dict


def APT_Behaviour_Extra_dict_sort_by_APT():
    Behaviour_Extra_dict_sort_by_APT = {}
    Behaviour_Extra_dict = Load_Result('Behaviour_Extra_dict')
    for APT in APT_list:
        file_extra_dict = Behaviour_Extra_dict[APT]
        file_list = file_extra_dict.keys()
        if len(file_list) == 0:
            Behaviour_Extra_dict_sort_by_APT.update({APT: {}})
        temp_extra = []
        for file in file_list:
            if len(file_extra_dict[file]) == 0:
                continue
            temp_extra.extend(file_extra_dict[file])
        temp_extra = list(set(temp_extra))
        Behaviour_Extra_dict_sort_by_APT.update({APT:temp_extra})
    return Behaviour_Extra_dict_sort_by_APT


def APT_Behaviour_Process_dict_sort_by_file():
    Behaviour_Process_dict = {}
    for APT in APT_list:
        temp_dir = root_dir + '/' + APT
        json_files = os.listdir(temp_dir)
        temp_process_dict = {}
        Behaviour_Process_dict.update({APT: {}})
        for json_file in json_files:
            with open(temp_dir + '/' + json_file, 'r') as load_f:
                temp_json = json.load(load_f)
            temp_keys = temp_json.keys()
            if not 'additional_info' in temp_keys:
                continue
            temp_additional_info = temp_json['additional_info']
            temp_keys = temp_additional_info.keys()
            if not 'behaviour-v1' in temp_keys:
                continue
            else:
                temp_behaviour_dict = temp_additional_info['behaviour-v1']
                temp_behaviour_keys = temp_behaviour_dict.keys()
                temp_behaviour_keys_list = tuple_to_list(temp_behaviour_keys)
                if not 'process' in temp_behaviour_keys_list:
                    continue
                else:
                    temp_file_process_dict = temp_behaviour_dict['process']
                    temp_process_keys = temp_file_process_dict.keys()
                    temp_pop_key_list = []
                    for key in temp_process_keys:
                        if len(temp_file_process_dict[key]) == 0:
                            temp_pop_key_list.append(key)
                    for key in temp_pop_key_list:
                        temp_file_process_dict.pop(key)
                    if len(temp_file_process_dict) == 0:
                        continue
                    else:
                        temp_process_dict.update({json_file: temp_file_process_dict})
        Behaviour_Process_dict.update({APT: temp_process_dict})
        print(APT, Behaviour_Process_dict)
        if len(Behaviour_Process_dict[APT]) != 0:
            print(Behaviour_Process_dict[APT])
    return Behaviour_Process_dict





def two_d_list_de_duplication(temp_hooking_list):
    if len(temp_hooking_list) == 0:
        return []
    final_list = temp_hooking_list[0]
    temp_hooking_list = temp_hooking_list[1:]
    for file_behaviour_hooking_list in temp_hooking_list:
        for behaviour_hooking in file_behaviour_hooking_list:
            if behaviour_hooking not in final_list:
                final_list.append(behaviour_hooking)
            else:
                continue
    return final_list


def tuple_to_list(tuple_ori):
    list_tar = []
    for tuple_element in tuple_ori:
        list_tar.append(tuple_element)
    return list_tar


def Write_Result(obj,name):
    with open(result_dir + name + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def Load_Result(name):
    with open(result_dir + name + '.pkl', 'rb') as f:
        return pickle.load(f)

def DeleteDuplicate(temp_dict):
    seen = set()
    new_dit = []
    for element_dict in temp_dict:
        t = tuple(element_dict.items())
        if t not in seen:
            seen.add(t)
            new_dit.append(element_dict)
    return new_dit




def Run_Script():
    # APT_Json_Count_list = APT_Json_Count()
    # print(APT_Json_Count_list)
    #
    #
    # APT_Json_Count_dict = APT_Json_Count_Dict()
    # print(APT_Json_Count_dict)
    # Write_Result(APT_Json_Count_dict,'APT_Json_Count_dict')
    #


    # test_dic = Load_Result('Behaviour_Extra_dict')
    # print(len(test_dic))
    # print(test_dic)


    # APT_Json_Count_dict_sorted = APT_Json_Count_Sort()
    # print(APT_Json_Count_dict_sorted)
    # Write_Result(APT_Json_Count_dict_sorted,'APT_Json_Count_dict_sorted')


    # APT_Related_URL_dict = APT_Related_URL()
    # print(APT_Related_URL_dict)
    # Write_Result( APT_Related_URL_dict,'APT_Related_URL_dict')


    # APT_Related_Domain_dict = APT_Related_Domain()
    # print(APT_Related_Domain_dict)
    # Write_Result(APT_Related_Domain_dict,'APT_Related_Domain_dict')


    # APT_Related_URL_dict_sorted = APT_Related_URL_Sort()
    # print(APT_Related_URL_dict_sorted)
    # Write_Result(APT_Related_URL_dict_sorted,'APT_Related_URL_dict_sorted')


    # APT_Related_Domain_dict_sorted = APT_Related_Domain_Sort()
    # print(APT_Related_Domain_dict_sorted)
    # Write_Result(APT_Related_Domain_dict_sorted,'APT_Related_Domain_dict_sorted')


    # APT_Related_URL_File_dict_sorted = APT_Related_URL_Sort_By_File()
    # print(APT_Related_URL_File_dict_sorted)
    # Write_Result(APT_Related_URL_File_dict_sorted,'APT_Related_URL_File_dict_sorted')


    # APT_Related_Domain_File_dict_sorted = APT_Related_Domain_Sort_By_File()
    # print(APT_Related_Domain_File_dict_sorted)
    # Write_Result(APT_Related_Domain_File_dict_sorted,'APT_Related_Domain_File_dict_sorted')


    # APT_Behaviour_list = Sample_Behaviour_list()
    # Write_Result(APT_Behaviour_list, 'APT_Behaviour_list')


    # Behaviour_Hooking_dict = APT_Behaviour_Hooking_dict()
    # Write_Result(Behaviour_Hooking_dict, 'Behaviour_Hooking_dict')


    # APT_Behaviour_Hooking_dict = APT_Behaviour_Hooking_dict_sort_by_APT()
    # Write_Result(APT_Behaviour_Hooking_dict, 'APT_Behaviour_Hooking_dict')


    # Behaviour_Network_dict = APT_Behaviour_Network_dict()
    # Write_Result(Behaviour_Network_dict, 'Behaviour_Network_dict')


    # Behaviour_Network_dict_sort_by_APT = APT_Network_Network_dict_sort_by_APT()
    # Write_Result(Behaviour_Network_dict_sort_by_APT, 'Behaviour_Network_dict_sort_by_APT')

    # Behaviour_Service_dict_sort_by_file = APT_Behaviour_Service_dict_sort_by_file()
    # Write_Result(Behaviour_Service_dict_sort_by_file, 'Behaviour_Service_dict_sort_by_file')

    # Behaviour_Service_dict_sort_by_APT = APT_Behaviour_Service_dict_sort_by_APT()
    # Write_Result(Behaviour_Service_dict_sort_by_APT, 'Behaviour_Service_dict_sort_by_APT')

    # Behaviour_Extra_dict = APT_Behaviour_Extra_dict_sort_by_file()
    # Write_Result(Behaviour_Extra_dict, 'Behaviour_Extra_dict')

    # Behaviour_Extra_dict_sort_by_APT = APT_Behaviour_Extra_dict_sort_by_APT()
    # Write_Result(Behaviour_Extra_dict_sort_by_APT, 'Behaviour_Extra_dict_sort_by_APT')

    Behaviour_Process_dict = APT_Behaviour_Process_dict_sort_by_file()
    Write_Result(Behaviour_Process_dict, 'Behaviour_Process_dict')




    pass


def Check_If_DS_Store():
    for file in APT_list:
        if file.find('DS') >=0:
            print('DS_Store')
            exit()
        else:
           continue
    print('DS_Store deleted')

if __name__ == '__main__':
    Check_If_DS_Store()
    Run_Script()
