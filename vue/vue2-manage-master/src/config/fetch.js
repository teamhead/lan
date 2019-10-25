import axios from 'axios';
let baseUrl = process.env.NODE_ENV == 'development' ? '/api' : 'http://sqlmanager.e6gpshk.com/api';
axios.interceptors.response.use(function (response) {
    // 对响应数据做点什么
    if (response.status === 200) {
		return response.data;
	} else {
		console.log("请求错误");
	}
  }, function (error) {
    // 对响应错误做点什么
    return Promise.reject(error);
  });
  axios.interceptors.request.use(function (config) {
	config.headers = {
		'Content-Type': 'application/json;charset=UTF-8'
	}
    return config;
  }, function (error) {
    // 对请求错误做些什么
    return Promise.reject(error);
  });
export const $http = (url='', data={}, type='get') => {
    url = `${baseUrl}${url}`
	if('get' === type.toLowerCase()) {
		return axios.get(url, data);
	}
	if('post' === type.toLowerCase()) {
		return axios.post(url , data)
	}
}
