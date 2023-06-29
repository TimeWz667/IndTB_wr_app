function fmt_percent(x) {
    return Math.round(x * 100) + "%"
}


export default [
    {
        Name: "PPM",
        Desc: "Private-public mixing",
        Clicked: false,
        Pars: [
            {
                name: "Scale", label: "New engaged private", type: "float", value:0, min: 0, max: 1, step:0.05,
                fmt: fmt_percent
            }
        ]
    },
    {
        Name: "CS",
        Desc: "Facilitate care-seeking",
        Clicked: false,
        Pars: [
            {
                name: "Scale", label: "Delay - ", type: "float", value:0, min: 0, max: 1, step:0.05,
                fmt: fmt_percent
            }
        ]
    },
    {
        Name: "ImpDx",
        Desc: "Improved TB diagnosis",
        Clicked: false,
        Pars: [
            {
                name: "Dx", label: "Diagnosis per visit", type: "float", value:0, min: 0, max: 1, step:0.05,
                fmt: fmt_percent
            }
        ]
    },
    {
        Name: "TPT",
        Desc: "TB preventive therapy",
        Clicked: false,
        Pars: [
            {
                name: "Scale", label: "Traced per index case", type: "int", value:0, min: 0, max: 50, step: 1,
                fmt: function(x) { return Math.round(x) }
            }
        ]
    },
    {
        Name: "TxCom",
        Desc: "Treatment completion",
        Clicked: false,
        Pars: [
            {
                name: "Scale", label: "Reduction in incomplete tx", type: "float", value:0, min: 0, max: 1, step: 0.05,
                fmt: fmt_percent
            }
        ]
    },
    {
        Name: "TxDie",
        Desc: "Treatment die",
        Clicked: false,
        Pars: [
            {
                name: "Scale", label: "Reduction in death on tx", type: "float", value:0, min: 0, max: 1, step: 0.05,
                fmt: fmt_percent
            }
        ]
    },
    {
        Name: "Vac",
        Desc: "Post-exposure vaccination",
        Clicked: false,
        Pars: [
            {
                name: "Efficacy", label: "Vaccine efficacy", type: "float", value:0, min: 0, max: 1, step: 0.05,
                fmt: fmt_percent
            },
            {
                name: "Coverage", label: "Coverage", type: "float", value:0, min: 0, max: 0.9, step: 0.05,
                fmt: fmt_percent
            }
        ]
    },
    {
        Name: "ACF",
        Desc: "Active case-finding",
        Clicked: false,
        Pars: [
            {
                name: "Yield", label: "Yield", type: "int", value:0, min: 0, max: 40, step: 1,
                fmt: function(x) { return Math.round(x) }
            },
            {
                name: "Asym", label: "Asymptomatic TB covered", value: false, type: "bool", fmt: x => x
            },
            {
                name: "Target", label: "Target population", type: "choice", value: 'All', values: ['All', '30%', '20%', '10%']
            }
        ]
    }
]
