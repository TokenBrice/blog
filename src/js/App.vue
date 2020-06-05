<template>
    <div>
        <div class="filters">
            <div v-for="(filters, index) in filtersList" :class="filters.class.toLowerCase()">
                <multiselect v-model="selectedFilters[index]" @input="getFilteredData" :options="filters.values"
                             :placeholder="filters.name" deselect-label="" select-label="" :multiple="true"
                             :searchable="false" :hide-selected="true"
                             label="name" track-by="name"></multiselect>
            </div>
        </div>
        <div class="media">
            <ul>
                <li v-for="medium in filteredData">
                    <p>
                        <a :href="medium.link" target="_blank" ref="noopener">{{ medium.name }}</a>
                    </p>
                </li>
            </ul>
        </div>
    </div>
</template>

<script>
    import media from '../../data/media.json'
    import filters from '../../data/filters.json'

    export default {
        data() {
            return {
                filteredData: [],
                language: null,
                filtersList: [],
                filters,
                selectedFilters: {
                    tags: [],
                    lang: [],
                    types: [],
                    date: [],
                },
            }
        },
        methods: {
            extractDateFromPosts: function () {
                media.forEach(item => {
                    if (item.date !== undefined && !this.filtersList["date"].values.find(date => date.name === item.date)) {
                        this.filtersList["date"].values.push({"key": item.date, "name": item.date});
                    }
                });
            },
            preselectActiveFilters: function () {
                for (const [key, category] of Object.entries(this.filtersList)) {
                    category.values.forEach(function (filter) {
                        if (filter.active !== undefined && filter.active) {
                            this.selectedFilters[key].push({"key": filter.key, "name": filter.name})
                        }
                    }, this)
                }
            },
            getFilteredData: function () {
                this.filteredData = media;
                let filteredDataByfilters = [];
                for (const [key, category] of Object.entries(this.selectedFilters)) {
                    if (category.length > 0) {
                        if (key === 'date') {
                            filteredDataByfilters = this.filteredData.filter(data => category.some(filter => data.date === filter.name));
                            this.filteredData = filteredDataByfilters;
                        } else {
                            if (category.length !== this.filtersList[key].values.length) {
                                filteredDataByfilters = this.filteredData.filter(data => category.some(filter => data.tags.includes(filter.key.toLowerCase())))
                                this.filteredData = filteredDataByfilters;
                            }
                        }
                    }
                }
            },
            getFiltersByLanguage: function () {
                switch (this.language) {
                    case "fr":
                        this.filtersList = this.filters.fr;
                        break;
                    default :
                        this.filtersList = this.filters.en;
                }
                this.extractDateFromPosts();

            }
        },
        mounted() {
            this.language = document.getElementById("language").value;
            this.getFiltersByLanguage();
            this.preselectActiveFilters();
            this.getFilteredData();
        }
    };
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>


<style>

    .multiselect__tags, .multiselect__input, .multiselect__content-wrapper {
        background: var(--color-bg);
    }

    .post ul.multiselect__content {
        padding-left: 0;
    }

    .multiselect__option--highlight, .multiselect__tag, .multiselect__option--selected {
        background: var(--color-primary);
        opacity: 0.8;
    }

    .multiselect__option.multiselect__option--highlight {
        color: #fff;
    }

    .multiselect__option--selected.multiselect__option--highlight {
        opacity: 0.7;
    }

    .multiselect__option {
        color: var(--color-contrast-high);
    }

    .multiselect__tag-icon:after {
        color: var(--color-primary-l);
    }

    .multiselect__tag-icon:focus, .multiselect__tag-icon:hover {
        background: var(--color-primary-h);
    }

    .filters {
        display: flex;
        align-items: flex-start;
        flex-wrap: wrap;
    }

    .tags {
        width: 100%;
    }

    .type, .lang, .tags, .date {
        margin: 10px 10px 0 0;
    }

    .type, .lang, .date {
        margin: 10px 10px 10px 0;
        flex: 1;

    }


</style>