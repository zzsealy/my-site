import global from "../Global.vue";
import axios from '../../http'

export default {
  getCates: function (){
    let cates = ''
    const path = global.URL + "/categories";
    return axios.get(path)
        
          }
}
