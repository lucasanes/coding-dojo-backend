from flask import Flask, request, jsonify # type: ignore

app = Flask(__name__)

def heapify(array,tamanho_heap,i):
    largest = i 
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < tamanho_heap and array[left] > array[largest]:
        largest = left
        
    if right < tamanho_heap and array[right] > array[largest]:
        largest = right
        
    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, tamanho_heap, largest)
        
def heapsort(array):
    tamanho_heap = len(array)
    
    for i in range(tamanho_heap // 2 - 1, -1, -1):
        heapify(array, tamanho_heap, i)
        
    for i in range(tamanho_heap - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
        
    return array

@app.route('/heapsort', methods=['POST'])
def ordenar():
    data = request.get_json()
    if 'array' not in data:
        return jsonify({'error': 'Array not provided'}), 400
    
    array = data['array']
    
    if not isinstance(array, list) or not all(isinstance(x, (int, float)) for x in array):
        return jsonify({'error': 'Invalid array format'}), 400
    
    sorted_array = heapsort(array)
    
    return jsonify({'sorted_array': sorted_array})
    
if __name__ == '__main__':
    app.run(debug=True)
