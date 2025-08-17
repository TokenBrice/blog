const webpack = require('webpack');
const path = require('path');
const {VueLoaderPlugin} = require('vue-loader');
const UglifyJsPlugin = require('uglifyjs-webpack-plugin')


module.exports = {
    entry: './src/js/main.js',
    mode: 'production',
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
        new VueLoaderPlugin(),
        new webpack.DefinePlugin({
            'process.env': {
                NODE_ENV: '"production"'
            }
        }),
    ],
    optimization: {
        minimizer: [
            new UglifyJsPlugin({
                uglifyOptions: {
                    warnings: false,
                    compress: {},
                    mangle: true, // Note `mangle.properties` is `false` by default.
                },
            }),
        ],
    },
    resolve: {
        alias: {
            vue: 'vue/dist/vue.esm.js'
        }
    }
};