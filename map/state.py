import json
from .database_operations import *
from array import *
from .arrays import *

def create_to_from(_to, _from):
    dates = []
    _to_day = _to[0] + _to[1]
    _to_month = _to[3] + _to[4]
    _to_year = _to[6] + _to[7] + _to[8] + _to[9]
    _from_day = _from[0] + _from[1]
    _from_month = _from[3] + _from[4]
    _from_year = _from[6] + _from[7] + _from[8] + _from[9]
    dates.append(_to_day)
    dates.append(_to_month)
    dates.append(_to_year)
    dates.append(_from_day)
    dates.append(_from_month)
    dates.append(_from_year)
    return dates


def return_state_categories_dataset(_state_id, _to, _from):
    categories_dataset = {}
    categories = []
    category_array = []
    dataset = []
    dataset1 = {}
    dataset2 = {}

    dataset1["seriesname"] = "Student-Teacher ratio"
    dataset2["seriesname"] = "Teacher Attendance Monitoring"

    data1 = []
    data2 = []

    districts = districts_in_state(_state_id)

    for i in range(0, len(districts)):
        district = districts[i]
        label_dict = {}
        label_dict['label'] = district.district_name + " - " + district.headquaters
        label_dict['link'] = "../mapdistrict?district=" + district.district_name + "&districtid=" + district.id + "&to=" + _to +"&from=" +_from
        category_array.append(label_dict)
        data1_ = {}
        data1_['value'] = i * 1000 + 2*i
        data1.append(data1_)
        data2_ = {}
        data2_['value'] = 2*i - 0.1 *i
        data2.append(data2_)


    dataset1["data"] = data1
    dataset2["data"] = data2
    dataset2["parentyaxis"] = "S"

    category = {}
    category['category'] = category_array
    categories.append(category)
    dataset.append(dataset1)
    dataset.append(dataset2)
    categories_dataset["categories"] = categories
    categories_dataset["dataset"] = dataset
    return categories_dataset


def return_state_chart(current_state, _to, _from):
    chart= {}
    chart["caption"] = current_state + " - Monitoring"
    if len(_from) != 0 and len(_to) != 0:
        chart["subCaption"] = _to + " : " + _from
    else:
        chart["subCaption"] = "For all the records"
    chart["pyaxisname"] = "Student teacher ratio"
    chart["syaxisname"] = "Attendance ratio"
    chart["xAxisName"] = "Cities"
    chart["showvalues"] = "0"
    chart["labelDisplay"] = "rotate"
    chart["slantLabel"] = "1"
    chart["formatNumberScale"] = "0"
    chart["sNumberPrefix"] = "$"
    chart["theme"] = "fint"
    return chart


def state_map_function(_state_id, _state, _to, _from):
    json_state = {}
    data_state = {}

    data_state['chart'] = return_state_chart(_state, _to, _from)
    categories_dataset = return_state_categories_dataset(_state_id, _to, _from)
    data_state['categories'] = categories_dataset["categories"]
    data_state['dataset'] = categories_dataset["dataset"]

    json_state["type"] = "mscombidy2d"
    json_state["renderAt"] = "chart-container"
    json_state["width"] = "800"
    json_state["height"] = "600"
    json_state["dataFormat"] = "json"
    json_state['dataSource'] = data_state

    return json.dumps(json_state)
