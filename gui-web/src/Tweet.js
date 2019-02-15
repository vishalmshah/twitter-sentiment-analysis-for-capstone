/* eslint-disable */

import React from 'react';
import './tweet.css';

const Tweet = ({ text }) => (
  <div class="tw-block-parent">
    <div class="timeline-TweetList-tweet">
      <div class="timeline-Tweet">
        <div class="timeline-Tweet-brand">
          <div class="Icon Icon--twitter"></div>
        </div>
        <div class="timeline-Tweet-author">
          <div class="TweetAuthor"><a class="TweetAuthor-link" href="#channel"> </a><span class="TweetAuthor-avatar"> 
              <div class="Avatar"> </div></span><span class="TweetAuthor-name">Sentiment Analysis Algorithm</span><span class="Icon Icon--verified"> </span><span class="TweetAuthor-screenName">@example</span></div>
        </div>
        <div class="timeline-Tweet-text"><p>{text}</p></div>
        <div class="timeline-Tweet-metadata"><span class="timeline-Tweet-timestamp">Xh</span></div>
        <ul class="timeline-Tweet-actions">
          <li class="timeline-Tweet-action"><a class="Icon Icon--heart" href="#"/></li>
          <li class="timeline-Tweet-action"><a class="Icon Icon--share" href="#"/></li>
        </ul>
      </div>
    </div>
  </div>
)

export default Tweet;
