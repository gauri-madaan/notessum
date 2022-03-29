import meaningcloud


def getSummarization(text, sentences):
    summary = ''
    print("\tGetting automatic summarization...")
    summarization_response = meaningcloud.SummarizationResponse(meaningcloud.SummarizationRequest('7b1bea0053576520ffcdefb5166de1c9', sentences=sentences, txt=text).sendReq())
    if summarization_response.isSuccessful():
        summary = summarization_response.getSummary()
    else:
        print("\tOops! Request to Summarization... was not successful: (" + summarization_response.getStatusCode() + ') ' + summarization_response.getStatusMsg())

    return summary
