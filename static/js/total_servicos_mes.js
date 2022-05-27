function total_cortes_tatuagens(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('total-cortes').innerHTML = data.total_cabelo
        document.getElementById('total-tatuagens').innerHTML = data.total_tatuagem
    })
}

