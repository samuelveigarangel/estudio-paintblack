function total_valor_mes(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('valor_mes').innerHTML = data.valor_mes
    })
}