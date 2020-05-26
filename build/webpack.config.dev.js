const webpack = require('webpack');
const path = require('path');
const {VueLoaderPlugin} = require('vue-loader');


module.exports = {
    entry: './src/js/main.js',
    mode: 'development',
    output: {
        path: path.resolve(__dirname, '../static/js'),
        filename: 'main.js',
    },
    module: {
        rules: [
            {
                test: /\.vue$/,
                use: {
                    loader: 'vue-loader',
                },
            },
            {
                test: /\.css$/,
                use: [
                    'vue-style-loader',
                    'css-loader'
                ],
            },
        ],
    },
    plugins: [
        new VueLoaderPlugin()
    ],
    resolve: {
        alias: {
            vue: 'vue/dist/vue.esm.js'
        }
    }
};