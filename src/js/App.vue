<template>
    <div>
        <div class="filters">
            <multiselect v-model="selectedFilters" @input="getFilteredData" :options="filtersList" deselect-label="" select-label="" :multiple="true" :searchable="false" :hide-selected="true"
                         label="name" track-by="name"></multiselect>
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
    import mediaEN from '../../data/media_en.json'
    import filters from '../../data/filters.json'
    import filtersEN from '../../data/filters_en.json'

    export default {
        name: 'Filters',
        data() {
            return {
                filteredData: [],
                language: null,
                filtersList: [],
                filters,
                filtersEN,
                selectedFilters: [],
            }
        },
        methods: {
            getFilteredData: function () {
                if (this.language === "fr") {
                    this.filteredData = media;
                } else {
                    this.filteredData = mediaEN;
                }
                let filteredDataByfilters = [];
                if (this.selectedFilters.length > 0) {
                    filteredDataByfilters = this.filteredData.filter(data => this.selectedFilters.every(filter => data.tags.includes(filter.key.toLowerCase())))
                    this.filteredData = filteredDataByfilters;
                }
            },
            getFiltersByLanguage: function () {
                switch (this.language) {
                    case "fr":
                        this.filtersList = this.filters;
                        break;
                    default :
                        this.filtersList = this.filtersEN;
                }

            }
        },
        mounted() {
            this.language = document.getElementById("language").value;
            this.getFiltersByLanguage();
            this.getFilteredData();

        }
    };
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"></style>


<style>

    .multiselect__tags, .multiselect__input, .multiselect__content-wrapper {
        background: var(--color-bg) ;
    }

    .post ul.multiselect__content {
        padding-left: 0;
    }

    .multiselect__option--highlight, .multiselect__tag, .multiselect__option--selected {
        background: var(--color-primary);
        opacity: 0.8;
    }

    .multiselect__option.multiselect__option--highlight {
        color:#fff;
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


</style>