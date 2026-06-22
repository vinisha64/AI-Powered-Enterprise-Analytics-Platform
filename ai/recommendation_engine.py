def generate_recommendations(kpis):
    recommendations = []

    if kpis["total_profit"] < 300000:
        recommendations.append(
            "Profit is relatively low. Consider reducing discounts."
        )

    if kpis["total_customers"] < 1000:
        recommendations.append(
            "Customer base can be expanded through marketing campaigns."
        )

    return recommendations