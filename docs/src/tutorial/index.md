<script setup>
  import txout from '../components/tutorial_txout.vue'
</script>


# Treatment outcome modelling


## Intro
In war-room model, the treatment process is determined by three rates outflowing from the compartments for those on treatment. 


## Preliminaries


#### Single event model
For a state (x) with a single outflow rate, ***r*** per year, the time to next event can be formulated as 
1 / r1.

In ODE model,
$$
\frac{dx}{dt} = - rx
$$
, and x is 1 initially for one person starting with the state.

The time spent in the state x is
$$
\int_0^{\infty}xdt = -\frac{1}{r}\int_0^{\infty}dx = \frac{1}{r}
$$
, where $\int_0^{\infty}dx = -1$
because there will be a person leave the state ultimately.


#### Multiple event model

For a compartment with two outflow rates, ***r1*** and ***r2*** per year, going toward respective events, ***e1*** and ***e2***, the two rates will compete for the next event.


In ODE model,
$$
\frac{dx}{dt} = - (r1 + r2)x
$$
, and x is 1 initially again for one person starting with the state.

Likewise, the time spent in the state x is 1 / (r1 + r2).

For the proportion going from x to e1, we focus on the net flow form x to e1, and integrate it over time

$$
\int_0^{\infty}(r1x) dt = \frac{r1}{r1 + r2} 
$$

Thus, for e2, the proportion is r2 / (r1 + r2)

In summary, for N people starting with state x, at the end point under ODE formulation

- every people ***1 / (r1 + r2)*** years before the next event regardless which event he/she is going to
- Probabilities for e1 and e2 are ***r1 / (r1 + r2)***, ***r2 / (r1 + r2)*** respectively 


## Back to treatment model

For simplicity, we grouped the treatment outcomes into three categories:

- Treatment completion (***TC***): including treatment successful
- Death during treatment period (***TD***)
- Others (***TL***): lost to follow-up, failed treatment, and other censored outcomes

and the rates to the events are ***rc***, ***rd***, and ***rl*** respectively.

What we have from data:

- 6 months time to treatment completion as the national guideline
  - We need ***1 / (rc + rd + rl) = 0.5***

- Proportions of each outcome after treatment initiated
  - Pr(TC) = ***rc / (rc + rd + rl)***
  - Pr(TD) = ***rd / (rc + rd + rl)***
  - Pr(TL) = ***rl / (rc + rd + rl)***


## Exercise
Assume no deaths during treatment, find the rates that match:

- 90% Treatment completion, 10% LTFU
- 6 months treatment period

::: info Try it
<txout></txout>
:::


