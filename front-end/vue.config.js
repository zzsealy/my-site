const webpack = require("webpack")
module.exports = {
    // 配置插件参数
    configureWebpack: {
        plugins: [
            // 配置 jQuery 插件的参数
            new webpack.ProvidePlugin({
                $: 'jquery',
                jQuery: 'jquery',
                'window.jQuery': 'jquery',
                Popper: ['popper.js', 'default']
            })
        ]
    }
}