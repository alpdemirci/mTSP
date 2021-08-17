# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 20:37:39 2021

@author: Alp
"""
import itertools
import json

"""
Algoritmanın kısa özeti:
    1- Verilen araç noktaları ve teslimat noktaları ayrı listelerde toplanır
    2- Teslimat listesi sırayla en yakın olan arca atanır ve aracın konumu
        teslimat yapılacak nokta ile değiştirilir. Böylelikle bidahaki teslimat
        noktası ilk teslimat noktasına yakınsa, 2. teslimatı da aynı araç
        yapacaktır
    3- Teslimat listesindeki sıralama önemli olacağı için bütün ihtimalleri
        değerlendirmek için teslimat listesinin bütün permütasyonları 2. adımda
        değerlendirilir
    4- İşlemler sonucunda toplam süre olarak sıralamak yerine geçen süre göz
        öndünde bulundurulmuştur. "Örnek vermek gerekirse 1. araç 3000 saniye,
        2.araç 2000 saniyeyse bu teslimatın süresi 3000 olarak ele alınmıştır."

        NOT: Teslimat süresi, servis süresi ile birlikte değerlendirilmiştir.
"""


def read_files(filename):
    """


    Parameters
    ----------
    filename : STR
    The json file name

    Returns
    -------
    araç : [location1,location2] type(araç[i]) = int
    Vehicles location in 1d array
    teslim : [destination1,destination2] type(teslim[i]) = int
    Destination location in 1d array
    matrix : 2d array
    Delivery duration between two location
    jobs : 1d array
    jobs list

    Description
    -------
    Bu fonksiyon gerekli verileri farklı formatlarda ayrıştırarak diğer
    fonksiyonlara hazırlmaktadır.

    """
    src = json.load(open(filename))
    matrix = src["matrix"]
    jobs = src["jobs"]
    vehicles = src["vehicles"]
    teslim = [d["location_index"]for d in jobs]  # teslim noktaların 1d matrisi
    araç = [d["start_index"]for d in vehicles]
    return araç, teslim, matrix, jobs


def create_veh_dict(vehicle):
    """


    Parameters
    ----------
    vehicle : [location1,location2] type(vehicle[i]) = int
    Vehicles location in 1d array

    Returns
    -------
    d : Dictionary
    {i : location..}

    Description
    -------
    Bu fonksiyon araçlara sırasıyla etiketlendirip başlangıç noktalarını tutan
    bir dictionary üretmektedir.
    """
    d = {}
    for i, e in enumerate(vehicle):
        d[str(i+1)] = [e]
    return d


def MTP(araç, teslim, matrix, service_dict):
    """


    Parameters
    ----------
    araç : [location1,location2] type(araç[i]) = int
    teslim : [destination1,destination2] type(teslim[i]) = int
    matrix :  2d array
    service_dict : Description

    Returns
    -------
    d : Dictionary
    dist_dict : Dictionary

    """
    d = create_veh_dict(araç)
    for e in teslim:
        distance = float("inf")
        for veh in d:
            son_nokta = d[veh][-1]
            dist = matrix[son_nokta][e] + service_dict[e]
            if dist < distance:
                araba = veh
                distance = dist
        d[araba].append(e)
    dist_dict = vehicle_and_distance(d, matrix, service_dict)
    return d, dist_dict


def vehicle_and_distance(dic, matrix, service_dict):
    """


    Parameters
    ----------
    dic : Dictionary
    matrix : 2d array
    service_dict : Dictionary

    Returns
    -------
    distance : Dictionary

    """
    distance = {}
    for e in dic:
        sum_way = 0
        destination = dic[e]
        for i in range(len(destination)-1):
            start, end = destination[i], destination[i+1]
            sum_way += matrix[start][end] + service_dict[end]
        distance[e] = sum_way
    return distance


def run_all_possible(filename):
    """


    Parameters
    ----------
    filename : STR
    The json file name

    Returns
    -------
    en_iyi_teslim : Result as dict

    """

    araç, teslim, matrix, jobs = read_files(filename)

    service_dict = service_duration_dict(jobs)
    duration = float("inf")
    liste = list(itertools.permutations(teslim))
    for e in liste:
        teslim = e
        d, dist_dict = MTP(araç, teslim, matrix, service_dict)
        if max(list(dist_dict.values())) < duration:
            en_iyi_teslim = d, dist_dict
            duration = max(list(dist_dict.values()))
    final_Dict = final_dict(en_iyi_teslim)
    return final_Dict


def service_duration_dict(jobs):
    """


    Parameters
    ----------
    jobs: 1d array

    Returns
    -------
    service_dict: Dictionary

    Description
    -----------
    Bu fonksiyon, görevlerdeki servis zamanlarını tutan bir dictionary üretir.

    """
    service_dict = {}
    for dic in jobs:
        service_dict[dic['location_index']] = dic['service']
    return service_dict


def final_dict(result_dict):
    """


    Parameters
    ----------
    result_dict : Dictionary

    Returns
    -------
    final_Dict : Dictionary

    Description
    -----------
    Bu fonksiyon output için gerekli formatı hazırlar.

    """
    routes, duration = result_dict[0], result_dict[1]
    for e in routes:
        routes[e] = routes[e][1:]
    final_Dict = {"total_delivery_duration": sum(list(duration.values())),
                  "routes": routes, "delivery_duration": duration}
    return final_Dict


filename = 'input.json'

result = run_all_possible(filename)
print(result)
