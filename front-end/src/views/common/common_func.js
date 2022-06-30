import {store} from "../store.js";
import axios from '../../http'

export default {
  getCates: function (){
    let cates = ''
    const path = store.URL + "/categories";
    return axios.get(path)
        
          }
}
