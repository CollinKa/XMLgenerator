#creates and edit a dictionary compatible to XMLGenerator

class EditDictionary:
    def __init__(self):
      self.dictionary = {}

    def createRoot(self, root_name: str):
      return {root_name: None}

    def createDict(self, list1: list, list2: list):
        if len(list1) != len(list2):
            raise ValueError("Lists must have the same length.")
        return {key: value for key, value in zip(list1, list2)}

    def _findKeyInList(self, lst: list, key_to_find: str):
        for index, item in enumerate(lst):
            if isinstance(item, dict) and key_to_find in item:
                return index, key_to_find
        return None, None

    def pathFinder(self, search_dictionary: dict, key_to_find: str):
        paths = []

        def searchInStructure(data, current_path=[]):
            if isinstance(data, dict):
                for key, value in data.items():
                    new_path = current_path + [key]
                    if key == key_to_find:
                        paths.append(new_path)
                    if isinstance(value, (dict, list)):
                        searchInStructure(value, new_path)
            elif isinstance(data, list):
                for index, item in enumerate(data):
                    new_path = current_path + [index]
                    if isinstance(item, (dict, list)):
                        searchInStructure(item, new_path)

        searchInStructure(search_dictionary)

        if not paths:
            raise KeyError(f"Key '{key_to_find}' not found in the dictionary.")

        return paths

    def pathNavigator(self, dictionary: dict, path: list):
        current = dictionary
        for key in path:
            if isinstance(current, dict) and key in current:
                current = current[key]
            elif isinstance(current, list):
                index, key_in_list = self._findKeyInList(current, key)
                if key_in_list is not None:
                    current = current[index][key_in_list]
                else:
                    break
            else:
                break
        return current

    def keyExist(self, dictionary: dict, key_to_check: str, path: list = None):
        if path is None:
            path = []
        if not path:
            return key_to_check in dictionary

        value_at_path = self.pathNavigator(dictionary, path)
        if value_at_path is None:
            return False

        if isinstance(value_at_path, dict):
            return key_to_check in value_at_path
        elif isinstance(value_at_path, list):
            try:
                key_index = int(key_to_check)
                return key_index >= 0 and key_index < len(value_at_path)
            except ValueError:
                return False

        return False

    def addDict(self, base_dictionary: dict, dict_to_add: dict, path=None):
        if not base_dictionary:
            raise ValueError("Base dictionary is empty.") 
        if path is None:
            if len(base_dictionary) > 1:
                raise ValueError("Base dictionary has more than one keys, please specify the path.")
            first_key = next(iter(base_dictionary))
            path = [first_key]

        current_dict = base_dictionary
        for idx, path_element in enumerate(path):
            if isinstance(path_element, str):
                if path_element in current_dict:
                    if idx == len(path) - 1:
                        final_key = path_element
                        if isinstance(current_dict[final_key], list):
                            current_dict[final_key].append(dict_to_add)
                        elif current_dict[final_key] is None:
                            current_dict[final_key] = {**dict_to_add}
                        elif isinstance(current_dict[final_key], dict) and next(iter(dict_to_add)) in current_dict[final_key]:
                            if not isinstance(current_dict[final_key], list):
                                current_dict[final_key] = [current_dict[final_key]]
                            current_dict[final_key].append(dict_to_add)
                        elif not isinstance(current_dict[final_key], dict):
                            current_dict[final_key] = [current_dict[final_key], dict_to_add]
                        else:
                            current_dict[final_key] = {**current_dict[final_key], **dict_to_add}
                    else:
                        current_dict = current_dict[path_element]
                else:
                    raise KeyError(f"Key '{path_element}' not found in the dictionary.")
            elif isinstance(path_element, int):
                if isinstance(current_dict, list) and 0 <= path_element < len(current_dict):
                    if idx == len(path) - 1:
                        final_index = path_element
                        current_dict[final_index].append(dict_to_add)
                    else:
                        current_dict = current_dict[path_element]
                else:
                    raise IndexError(f"Index '{path_element}' out of bounds or not a list.")
            else:
                raise ValueError("Path elements must be either strings or integers.")

    def visualizeDict(self, dictionary: dict, indent="", parent_key: str = None):
        if isinstance(dictionary, dict):
            keys = list(dictionary.keys())

            def _isLastKey(key):
                idx = keys.index(key)
                if parent_key is not None and parent_key in dictionary:
                    parent_idx = keys.index(parent_key)
                    return idx == len(keys) - 1 and parent_idx == len(keys) - 1
                return idx == len(keys) - 1

            for idx, key in enumerate(keys):
                tree_structure = " └─" if _isLastKey(key) else " ├─"
                line_connector = "   " if _isLastKey(key) else " │  "

                sub_structure = line_connector if idx == len(keys) - 1 else " │ "

                if isinstance(dictionary[key], (dict, list)):
                    print(indent + tree_structure + f"'{key}'")
                    self.visualizeDict(dictionary[key], indent + sub_structure, key)
                else:
                    value_str = f"'{dictionary[key]}'" if dictionary[key] is not None else "None"
                    print(indent + tree_structure + f"'{key}': {value_str}")
        elif isinstance(dictionary, list):
            for entry in dictionary:
                self.visualizeDict(entry, indent)
        else:
            value_str = f"'{dictionary}'" if dictionary is not None else "None"
            print(indent + value_str)


if __name__ == "__main__":
    editor = EditDictionary()

    # Example lists
    list1 = ["A", "B", "C"]
    list2 = ["1", "2", "3"]
    list3 = ["X", "Y", "Z"]
    list4 = ["4", "5", "6"]
    list5 = ["I", "J", "K"]
    list6 = ["7", "8", "9"]

    #create dictionaries using two lists
    dicta = editor.createDict(list1, list2)
    dictb = editor.createDict(list3, list4)
    dictc = editor.createDict(list5, list6)

    #print(dicta)
    print(dictb)
    #print(dictc)

    #create "root key", nesting each dictionary under a single key 
    dictA = editor.createRoot("sub")
    editor.addDict(dictA, dicta, ["sub"])

    dictB = editor.createRoot("sub")
    editor.addDict(dictB, dictb, ["sub"])

    dictC = editor.createRoot("sub")
    editor.addDict(dictC, dictc, ["sub"])
    
    editor.visualizeDict(dictB)
    

    #Create the root dictionary
    root_dict = {
        'Level1_Key1': {
            'Level2_Key1': {
                'Level3_Key1': 'Value1',
                'Level3_Key2': 'Value2'
            },
            'Level2_Key2': {
                'Level3_Key3': 'Value3',
                'Level3_Key4': 'Value4'
            }
        },
        'Level1_Key2': {
            'Level2_Key2': {
                'Level3_Key5': 'Value5',
                'Level3_Key6': 'Value6'
            },
            'Level2_Key3': {
                'Level3_Key7': 'Value7',
                'Level3_Key8': 'Value8'
            }
        },
        'Level1_Key3': [{
            'Level2_Key4': {
                'Level3_Key9': 'Value9',
                'Level3_Key10': 'Value10'
            },
            'Level2_Key5': {
                'Level3_Key11': 'Value11',
                'Level3_Key12': 'Value12'
            }
        },
        {
            'Level2_Key6': {
                'Level3_Key13': 'Value13',
                'Level3_Key14': 'Value14'
            },
            'Level2_Key7': {
                'Level3_Key15': 'Value15',
                'Level3_Key16': 'Value16'
            }
        }]
    }

    # visualizes the dictionary on the prompt
    editor.visualizeDict(root_dict)

    print()
    # find the "path" to a key in the root_dict
    # path consists of list of keys.
    path1 = editor.pathFinder(root_dict, 'Level3_Key3')
    print(path1)   # gives [['Level1_Key1', 'Level2_Key2', 'Level3_Key3']]


    path2 = editor.pathFinder(root_dict, 'Level2_Key2')
    print(path2)   # gives [['Level1_Key1', 'Level2_Key2'], ['Level1_Key2', 'Level2_Key2']]
    # Because there are two 'Level2_Key2' keys in root_dict


    path3 = editor.pathFinder(root_dict, 'Level3_Key15')
    print(path3)   # gives [['Level1_Key3', 1, 'Level2_Key7', 'Level3_Key15']]
    # that integer 1 in the list is the index. It's because the dictionary contains a list.


    # Add the dictionaries to the root dictionary
    editor.addDict(root_dict, dictA, path1[0])
    editor.addDict(root_dict, dictB, path2[1])  #this will choose ['Level1_Key2','Level2_Key2'] for path
    editor.addDict(root_dict, dictC, path2[1])
    editor.addDict(root_dict, dictA, path3[0])  
    # testing various different kinds of situations

    print()
    #visualize the resulting dictionary
    editor.visualizeDict(root_dict)
    print(root_dict)
